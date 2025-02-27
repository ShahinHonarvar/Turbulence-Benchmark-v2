def filter_chars(text):
    for i in range(170, 195):
        char = chr(i)
        if char > '!' and char < '}':
            text = text.replace(char, '')
    return text