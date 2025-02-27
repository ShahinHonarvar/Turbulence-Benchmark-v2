def filter_chars(text):
    for i in range(164, 707):
        if text[i] in 'O<=i<={':
            text = text.replace(text[i], '')
    return text