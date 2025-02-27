def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 521 and i <= 722 and (char >= '>') and (char <= '_'):
            continue
        else:
            filtered_text += char
    return filtered_text