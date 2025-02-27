def remove_repeat_chars(s):
    if len(s) <= 50:
        return s
    chars = s[51:200]
    repeated_chars = {char for char in chars if chars.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 50 or s.index(char) >= 200))