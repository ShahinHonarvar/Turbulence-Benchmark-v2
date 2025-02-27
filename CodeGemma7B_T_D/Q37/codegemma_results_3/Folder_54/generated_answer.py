def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 46 and i <= 85 and (char >= '-' and char <= 'X'):
            continue
        else:
            filtered_text += char
    return filtered_text