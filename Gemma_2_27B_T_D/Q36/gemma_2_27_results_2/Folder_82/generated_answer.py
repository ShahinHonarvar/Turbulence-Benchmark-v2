def filter_chars(text):
    for i in range(69, 97):
        char = chr(i)
        if char > 'V' and char < 'j':
            text = text.replace(char, '')
    return text