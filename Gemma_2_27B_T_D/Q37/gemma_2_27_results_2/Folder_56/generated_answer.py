def filter_chars(text):
    for i in range(71, 95):
        char = chr(i)
        if char >= 'K' and char <= 'a':
            text = text.replace(char, '')
    return text