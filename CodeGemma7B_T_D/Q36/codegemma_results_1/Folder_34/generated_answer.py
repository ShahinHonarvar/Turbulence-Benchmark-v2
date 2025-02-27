def filter_chars(text):
    filtered_text = text[:10]
    for i in range(10, 79):
        if text[i] > '?' and text[i] < 'm':
            filtered_text += text[i]
    filtered_text += text[79:]
    return filtered_text