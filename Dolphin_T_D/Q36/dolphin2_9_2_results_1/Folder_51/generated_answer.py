def filter_chars(text):
    for c in range(58, 81):
        if text[c] > '5' and text[c] < '>':
            text = text.replace(text[c], '')
    return text