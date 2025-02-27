def filter_chars(text):
    for i in range(26, 80):
        char = chr(i)
        if char > '<' and char < '>':
            text = text.replace(char, '')
    return text