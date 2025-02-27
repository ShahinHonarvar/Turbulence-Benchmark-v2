def filter_chars(text):
    for i in range(38, 55):
        if i < len(text):
            char = text[i]
            if char >= ':' and char <= 'r':
                text = text.replace(char, '')
    return text