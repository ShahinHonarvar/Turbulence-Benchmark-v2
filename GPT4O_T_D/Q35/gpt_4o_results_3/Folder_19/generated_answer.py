def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    sub_str = s[2:4]
    repeating_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = ''.join((char for char in s if char not in repeating_chars))
    return result