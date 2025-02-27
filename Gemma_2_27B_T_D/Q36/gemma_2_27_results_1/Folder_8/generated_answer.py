def filter_chars(text):
    for i in range(82, 93):
        char = text[i]
        if char > '!' and char < '*':
            text = text.replace(char, '')
    return text