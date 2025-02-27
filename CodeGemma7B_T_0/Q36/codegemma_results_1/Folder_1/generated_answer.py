def filter_chars(text):
    for i in range(69, 87):
        if text[i] > '#' and text[i] < 'L':
            text = text.replace(text[i], '')
    return text