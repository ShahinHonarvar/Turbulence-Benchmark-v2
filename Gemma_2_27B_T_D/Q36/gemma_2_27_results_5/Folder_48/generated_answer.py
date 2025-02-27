def filter_chars(text):
    for i in range(154, 222):
        char = chr(i)
        if char > 'A' and char < 'f':
            text = text.replace(char, '')
    return text