def filter_chars(text):
    filtered_text = ''
    for i in range(len(text)):
        char = text[i]
        if not (41 <= i <= 86 and 'S' <= char <= 's'):
            filtered_text += char
    return filtered_text