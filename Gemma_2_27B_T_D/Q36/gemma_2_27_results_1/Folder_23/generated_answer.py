def filter_chars(text):
    for i in range(21, 25):
        if len(text) > i:
            char = text[i]
            if char > '5' and char < '}':
                text = text.replace(char, '')
    return text