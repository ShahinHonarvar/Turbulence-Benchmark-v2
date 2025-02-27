def filter_chars(text):
    for i in range(69, 81):
        if i < len(text):
            for char in text[i:]:
                if char >= '@' and char <= 'p':
                    text = text.replace(char, '')
    return text