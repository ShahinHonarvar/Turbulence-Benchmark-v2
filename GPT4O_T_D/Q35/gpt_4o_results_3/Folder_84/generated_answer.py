def remove_repeat_chars(s):
    sub_str = s[33:44]
    repeated_chars = {char for char in set(sub_str) if sub_str.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))