def remove_repeat_chars(s):
    substring = s[20:35]
    repeat_chars = [char for char in substring if substring.count(char) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s