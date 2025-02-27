def remove_repeat_chars(s):
    chars_to_remove = set(s[20:43])
    for char in chars_to_remove:
        if s[20:43].count(char) > 1:
            s = s.replace(char, '', s[20:43].index(char))
    return s