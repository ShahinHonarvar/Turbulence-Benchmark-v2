def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if 15 <= i <= 55 and 'W' <= char <= '{':
            continue
        filtered_text += char
    return filtered_text