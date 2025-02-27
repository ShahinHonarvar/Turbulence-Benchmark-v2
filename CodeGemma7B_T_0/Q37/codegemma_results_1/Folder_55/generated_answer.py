def filter_chars(text):
    for i in range(1, 6):
        if text[i] in string.ascii_letters and text[i] >= '$' and (text[i] <= ';'):
            text = text.replace(text[i], '')
    return text