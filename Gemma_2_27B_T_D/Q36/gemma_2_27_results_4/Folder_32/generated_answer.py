def filter_chars(text):
    for i in range(40, 63):
        char = chr(i)
        if char > '7' and char < 'H':
            text = text.replace(char, '')
    return text