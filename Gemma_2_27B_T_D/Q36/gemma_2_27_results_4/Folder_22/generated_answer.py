def filter_chars(text):
    for i in range(55, 84):
        char = chr(i)
        if char > ';' and char < 'z':
            text = text.replace(char, '')
    return text