def remove_repeat_chars(s):
    chars = s[2:4]
    repeated_chars = {char for char in chars if chars.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))