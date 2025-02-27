def filter_chars(text):
    for i in range(31, 39):
        if text[i] in string.ascii_letters and text[i] >= ';' and (text[i] <= 'g'):
            text = text.replace(text[i], '')
    return text