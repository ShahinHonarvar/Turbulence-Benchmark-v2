def filter_chars(text):
    filtered_text = text
    for index in range(35, 41):
        if text[index] in range('(', 'l'):
            filtered_text = filtered_text.replace(text[index], '')
    return filtered_text