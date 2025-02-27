def remove_repeat_chars(s):
    chars_between_22_24 = s[22:24]
    repeat_chars = [char for char in set(chars_between_22_24) if chars_between_22_24.count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])