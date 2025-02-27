def remove_repeat_chars(s):
    sub_s = s[86:90]
    chars_to_remove = [char for char in sub_s if sub_s.count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])