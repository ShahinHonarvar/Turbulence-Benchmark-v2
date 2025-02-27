def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 1 and i <= 7 and (char >= 'L') and (char <= 'a'):
            continue
        filtered_text += char
    return filtered_text