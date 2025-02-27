def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 515 <= i <= 538 and '+' <= char <= '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s