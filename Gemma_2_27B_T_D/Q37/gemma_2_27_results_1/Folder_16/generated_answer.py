def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            continue
        filtered_text += char
    return filtered_text