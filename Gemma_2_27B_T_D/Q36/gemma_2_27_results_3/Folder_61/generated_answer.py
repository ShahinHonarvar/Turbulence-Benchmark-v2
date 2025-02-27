def filter_chars(text):
    for i in range(3, 9):
        char = text[i]
        if char > '*' and char < 'E':
            text = text.replace(char, '')
    return text