def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 515 and i <= 538 and (char >= '+') and (char <= '}'):
            continue
        filtered_text += char
    return filtered_text