def filter_chars(text):
    for i in range(18, 38):
        char = text[i]
        if char > ')' and char < 'P':
            text = text.replace(char, '')
    return text