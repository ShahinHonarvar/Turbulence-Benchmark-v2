def remove_repeat_chars(s):
    sub_string = s[34:78]
    repeated_chars = {char for char in sub_string if sub_string.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 33 or s.index(char) >= 78))