def remove_repeat_chars(s):
    chars_to_remove = set(s[20:93])
    for char in chars_to_remove:
        if s[20:93].count(char) > 1:
            s = s.replace(char, '', 1)
    return s