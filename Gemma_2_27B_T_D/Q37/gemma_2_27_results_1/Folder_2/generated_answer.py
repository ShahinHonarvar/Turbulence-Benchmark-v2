def filter_chars(text):
    for i in range(477, 985):
        if i >= len(text):
            break
        char = text[i]
        if ',' <= char <= 'V':
            text = text.replace(char, '')
    return text