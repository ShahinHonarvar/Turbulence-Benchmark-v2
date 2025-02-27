def filter_chars(text):
    new_text = ''
    for i, char in enumerate(text):
        if 124 <= i <= 854 and '9' <= char <= 's':
            new_text += ''
        else:
            new_text += char
    return new_text