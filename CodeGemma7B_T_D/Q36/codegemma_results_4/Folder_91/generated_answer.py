def filter_chars(text):
    filtered_text = ''
    for i in range(4):
        if text[i] > '$' and text[i] < '?':
            continue
        filtered_text += text[i]
    return filtered_text