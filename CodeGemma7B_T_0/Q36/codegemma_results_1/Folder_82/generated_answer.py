def filter_chars(text):
    for i in range(69, 97):
        if text[i] > 'V' and text[i] < 'j':
            text = text.replace(text[i], '')
    return text