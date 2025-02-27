def filter_chars(text):
    new_text = list(text)
    for index, char in enumerate(text):
        if 12 <= index <= 88 and '&' <= char <= 'v':
            new_text.remove(char)
    return ''.join(new_text)