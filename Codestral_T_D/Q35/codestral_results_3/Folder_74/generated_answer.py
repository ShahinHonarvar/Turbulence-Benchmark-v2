def remove_repeat_chars(s):
    chars = s[69:97]
    chars_to_remove = {char for char in chars if chars.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))