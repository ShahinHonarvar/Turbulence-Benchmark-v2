def filter_chars(text):
    for i in range(88, 91):
        if text[i] in 'JQL':
            text = text.replace(text[i], '')
    return text