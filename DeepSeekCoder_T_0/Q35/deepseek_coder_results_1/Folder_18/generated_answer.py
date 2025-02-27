def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    sub_str = s[56:90]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = ''.join([char for char in s if char not in repeat_chars])
    return result