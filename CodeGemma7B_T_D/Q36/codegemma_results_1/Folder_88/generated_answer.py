def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 78 or i >= 81 or char not in ['S', '[', '>']:
            filtered_text += char
    return filtered_text