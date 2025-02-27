def remove_repeat_chars(s):
    sub_str = s[38:43]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 37 or s.index(char) >= 43))