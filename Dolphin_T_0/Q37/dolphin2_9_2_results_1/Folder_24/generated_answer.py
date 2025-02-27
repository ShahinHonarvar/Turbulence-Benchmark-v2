def filter_chars(text):
    for cha in range(36, 80):
        if text[cha] >= '2' and text[cha] <= 's':
            text = text.replace(text[cha], '')
    return text