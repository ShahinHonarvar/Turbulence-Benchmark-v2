def filter_chars(text):
    for i in range(12, 78):
        if ':' <= text[i] <= 'L':
            text = text.replace(text[i], '')
    return text