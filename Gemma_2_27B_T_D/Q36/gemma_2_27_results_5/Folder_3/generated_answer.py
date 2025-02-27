def filter_chars(text):
    for i in range(42, 78):
        char = text[i]
        if char > '!' and char < '?':
            text = text.replace(char, '')
    return text