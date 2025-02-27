def insert_before_character(text):
    for i, char in enumerate(text):
        if char == 'u':
            text = text[:i] + 'U' + text[i:]
    return text