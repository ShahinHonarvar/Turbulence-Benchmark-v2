def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if 51 <= i <= 96 and 'X' <= char <= 'p':
            text = text.replace(char, '')
        filtered_text += char
    return filtered_text