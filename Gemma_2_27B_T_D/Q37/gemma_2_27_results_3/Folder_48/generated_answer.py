def filter_chars(text):
    for i in range(513, 878):
        if len(text) > i and '?' <= text[i] <= 'n':
            text = text.replace(text[i], '')
    return text