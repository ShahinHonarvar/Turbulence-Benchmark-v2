def filter_chars(text):
    for i in range(384, 412):
        if i < len(text) and '/' <= text[i] <= '8':
            text = text.replace(text[i], '')
    return text