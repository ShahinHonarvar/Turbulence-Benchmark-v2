def filter_chars(text):
    for i in range(19, 23):
        if i < len(text):
            char = text[i]
            if char >= ']' and char <= 't':
                text = text.replace(char, '')
    return text