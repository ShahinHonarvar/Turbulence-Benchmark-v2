def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sub_str = s[40:43]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))