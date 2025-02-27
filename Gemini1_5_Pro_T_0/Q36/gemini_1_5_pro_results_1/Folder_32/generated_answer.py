def filter_chars(text):
    for i in range(40, 63):
        if i >= len(text):
            break
        if text[i] > '7' and text[i] < 'H':
            text = text.replace(text[i], '')
    return text