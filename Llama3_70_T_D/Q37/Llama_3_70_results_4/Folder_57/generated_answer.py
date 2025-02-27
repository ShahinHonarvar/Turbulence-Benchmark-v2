def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 27 <= i <= 85 and '!' <= char <= 'B']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s