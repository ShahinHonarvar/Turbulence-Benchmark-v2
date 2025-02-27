def filter_chars(s):
    chars_to_remove = [char for char in s[54:63] if ord(')') <= ord(char) <= ord('9')]
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s