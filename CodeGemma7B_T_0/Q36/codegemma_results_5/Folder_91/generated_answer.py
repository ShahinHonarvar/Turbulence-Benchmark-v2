def filter_chars(text):
    filtered_text = ''
    for i in range(4):
        if text[i] > '$' and text[i] < '?':
            filtered_text += text[i]
    for i in range(4, len(text)):
        filtered_text += text[i]
    return filtered_text