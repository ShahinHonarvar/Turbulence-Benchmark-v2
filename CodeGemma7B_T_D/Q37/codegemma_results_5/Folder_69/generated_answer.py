def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 114 and i <= 639 and (char >= '!') and (char <= 'x'):
            pass
        else:
            filtered_text += char
    return filtered_text