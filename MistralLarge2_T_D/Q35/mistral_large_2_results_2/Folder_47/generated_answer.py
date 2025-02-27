def remove_repeat_chars(s):
    indices = range(29, 53)
    chars_to_remove = {char for i, char in enumerate(s) if i in indices}.intersection((char for char in s[29:53] if s[29:53].count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))