def remove_repeat_chars(s):
    start, end = (56, 88)
    sub_str = s[start:end]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result