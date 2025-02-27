def filter_chars(s):
    chars_to_remove = [char for index, char in enumerate(s) if 19 <= index <= 92 and '8' <= char <= 'm']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s