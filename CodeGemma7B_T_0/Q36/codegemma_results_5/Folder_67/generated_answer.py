def filter_chars(text):
    for i in range(18, 31):
        if text[i] > 'H' and text[i] < '|':
            text = text.replace(text[i], '')
    return text