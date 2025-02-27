def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 81 or i >= 89 or (char > 'f' and char < '{'):
            filtered_text += char
    return filtered_text