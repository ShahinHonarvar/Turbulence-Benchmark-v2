def filter_chars(text):
    for i in range(1, 7):
        char = text[i]
        if char > '-' and char < 'L':
            text = text.replace(char, '')
    return text