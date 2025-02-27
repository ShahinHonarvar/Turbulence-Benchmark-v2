def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 13 or i >= 40:
            filtered_text += char
            continue
        if char > ':' and char < 'C':
            pass
        else:
            filtered_text += char
    return filtered_text