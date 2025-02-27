def filter_chars(text):
    new_text = ''
    for i, char in enumerate(text):
        if not (477 <= i <= 984 and ',' <= char <= 'V'):
            new_text += char
    return new_text