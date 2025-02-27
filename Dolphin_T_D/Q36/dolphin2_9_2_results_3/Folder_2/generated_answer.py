def filter_chars(text):
    filter_chars_loc = range(421, 854)
    filter_chars_remove = []
    for idx, char in enumerate(text):
        if idx in filter_chars_loc and 'D' < char < 'J':
            filter_chars_remove.append(char)
    for char in filter_chars_remove:
        text = text.replace(char, '')
    return text