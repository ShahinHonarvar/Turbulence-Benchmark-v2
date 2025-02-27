def filter_chars(text):
    for i in range(19, 69):
        char = text[i]
        if char > '<' and char < 'C':
            text = text.replace(char, '')
    return text