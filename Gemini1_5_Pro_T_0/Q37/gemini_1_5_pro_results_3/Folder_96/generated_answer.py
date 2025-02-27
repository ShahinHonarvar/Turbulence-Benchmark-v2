def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        char = text[i]
        if not (86 <= i <= 92 and '!' <= char <= 's'):
            filtered_text += char
    return filtered_text