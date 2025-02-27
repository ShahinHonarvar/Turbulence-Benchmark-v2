def remove_repeat_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 34 < i < 69 and s.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))