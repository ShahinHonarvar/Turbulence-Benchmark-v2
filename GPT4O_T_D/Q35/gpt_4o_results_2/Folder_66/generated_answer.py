def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    part = s[12:76]
    repeated_chars = {char for char in part if part.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 11 or s.index(char) >= 76))