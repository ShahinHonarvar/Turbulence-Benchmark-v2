def filter_chars(text):
    for i in range(43, 69):
        char = text[i]
        if char > 'B' and char < 'r':
            text = text.replace(char, '')
    return text