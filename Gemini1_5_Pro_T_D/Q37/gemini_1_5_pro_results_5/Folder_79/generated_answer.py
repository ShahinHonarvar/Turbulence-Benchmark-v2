def filter_chars(text):
    for i in range(10, 53):
        if i <= len(text) - 1:
            if text[i] >= '@' and text[i] <= 'T':
                text = text.replace(text[i], '')
    return text