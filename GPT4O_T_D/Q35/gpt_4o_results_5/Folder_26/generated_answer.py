def remove_repeat_chars(s):
    chars_between = s[69:99]
    repeated_chars = {char for char in chars_between if chars_between.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))