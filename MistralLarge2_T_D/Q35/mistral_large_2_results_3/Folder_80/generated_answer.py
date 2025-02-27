def remove_repeat_chars(s):
    sub_str = s[57:84]
    chars_to_remove = {char for char in sub_str if sub_str.count(char) > 1}
    return ''.join([char for char in s if char not in chars_to_remove])