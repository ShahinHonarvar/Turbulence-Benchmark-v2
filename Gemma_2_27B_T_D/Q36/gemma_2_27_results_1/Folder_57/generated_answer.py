def filter_chars(text):
    for i in range(70, 74):
        if len(text) > i:
            char = text[i]
            if 'A' < char < 'U':
                text = text.replace(char, '')
    return text