def remove_repeat_chars(s):
    to_remove = {char for idx, char in enumerate(s) if 40 < idx < 200 and s.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))