def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if 29 <= i <= 97 and char in '-n':
            filtered_text += char
    return filtered_text