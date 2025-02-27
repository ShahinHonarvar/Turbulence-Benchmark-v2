def filter_chars(text):
    for i in range(72, 93):
        char = chr(i)
        if char > '<' and char < 'J':
            text = text.replace(char, '')
    return text