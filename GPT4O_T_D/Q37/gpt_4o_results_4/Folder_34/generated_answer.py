def filter_chars(s):
    if len(s) < 63:
        return s
    filter_range = s[54:63]
    chars_to_remove = {char for char in filter_range if ')' <= char <= '9'}
    return ''.join((char for char in s if char not in chars_to_remove))