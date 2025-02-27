def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 11 <= i <= 32 and '!' <= char <= '@']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s