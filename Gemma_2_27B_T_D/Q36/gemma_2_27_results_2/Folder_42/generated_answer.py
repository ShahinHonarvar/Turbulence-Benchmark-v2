def filter_chars(text):
    for i in range(42, 68):
        char = text[i]
        if char > 't' and char < 'x':
            text = text.replace(char, '')
    return text