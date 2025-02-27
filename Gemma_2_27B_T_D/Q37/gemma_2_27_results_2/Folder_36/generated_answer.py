def filter_chars(text):
    for i in range(259, 503):
        if len(text) > i and ',' <= text[i] <= '3':
            text = text.replace(text[i], '')
    return text