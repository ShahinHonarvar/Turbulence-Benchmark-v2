def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 69 and i <= 80 and (char >= '@') and (char <= 'p'):
            continue
        filtered_text += char
    return filtered_text