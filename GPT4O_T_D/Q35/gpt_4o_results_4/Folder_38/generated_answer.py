def remove_repeat_chars(s):
    sub_string = s[37:85]
    repeat_chars = {char for char in sub_string if sub_string.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 36 or s.index(char) >= 85))