def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 12 and i <= 88 and (char >= '&') and (char <= 'v'):
            continue
        filtered_text += char
    return filtered_text