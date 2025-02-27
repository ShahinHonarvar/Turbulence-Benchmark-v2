def filter_chars(text):
    for i in range(42, 68):
        if len(text) > i:
            char = text[i]
            if char > 't' and char < 'x':
                text = text.replace(char, '')
    return text