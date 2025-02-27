def filter_chars(text):
    for i in range(31, 73):
        char = chr(i)
        if char > 'M' and char < 'j':
            text = text.replace(char, '')
    return text