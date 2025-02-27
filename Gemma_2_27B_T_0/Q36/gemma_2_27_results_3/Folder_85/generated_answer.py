def filter_chars(text):
    for i in range(55, 80):
        char = chr(i)
        if char > 'S' and char < 's':
            text = text.replace(char, '')
    return text