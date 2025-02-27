def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 83 and i <= 99 and (char >= '*') and (char <= 'j'):
            continue
        else:
            filtered_text += char
    return filtered_text