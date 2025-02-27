def remove_repeat_chars(s):
    chars_to_remove = {char for idx, char in enumerate(s) if 10 < idx < 79 and s.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))