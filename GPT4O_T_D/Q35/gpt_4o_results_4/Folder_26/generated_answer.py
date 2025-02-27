def remove_repeat_chars(s):
    if len(s) < 99:
        return s
    sub_str = s[69:99]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))