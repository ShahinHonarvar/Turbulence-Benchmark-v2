def remove_repeat_chars(s):
    chars_to_remove = set(s[73:84])
    for char in chars_to_remove:
        if s[73:84].count(char) > 1:
            s = s.replace(char, '', s[73:84].index(char) + 73)
    return s