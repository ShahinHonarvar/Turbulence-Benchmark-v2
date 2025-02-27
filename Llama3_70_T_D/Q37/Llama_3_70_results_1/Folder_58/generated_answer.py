def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 503 <= i <= 753 and '9' <= char <= 'w']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s