def filter_chars(text):
    for i in range(299, 418):
        char = text[i]
        if char > '9' and char < 'P':
            text = text.replace(char, '')
    return text