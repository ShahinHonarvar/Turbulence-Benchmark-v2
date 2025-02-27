def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if 35 <= i <= 89 and 'E' <= char <= 't':
            text = text.replace(char, '')
        filtered_text += char
    return filtered_text