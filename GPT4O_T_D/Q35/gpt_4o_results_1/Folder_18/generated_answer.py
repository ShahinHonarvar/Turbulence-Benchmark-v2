def remove_repeat_chars(s):
    sub_str = s[56:91]
    repeat_chars = {char for char in sub_str[1:-1] if sub_str.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars or not 57 <= s.index(char) < 90))