def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 36 and i <= 79 and (char >= 'a') and (char <= 'i'):
            continue
        else:
            filtered_text += char
    return filtered_text