def filter_chars(text):
    for i in range(43, 83):
        char = text[i]
        if char > ':' and char < 'Q':
            text = text.replace(char, '')
    return text