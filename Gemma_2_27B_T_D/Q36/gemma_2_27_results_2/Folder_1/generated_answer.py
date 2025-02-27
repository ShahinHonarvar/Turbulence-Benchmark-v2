def filter_chars(text):
    for i in range(69, 87):
        char = chr(i)
        if char > '#' and char < 'L':
            text = text.replace(char, '')
    return text