def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        if i not in range(4, 8):
            filtered_text += text[i]
    return filtered_text