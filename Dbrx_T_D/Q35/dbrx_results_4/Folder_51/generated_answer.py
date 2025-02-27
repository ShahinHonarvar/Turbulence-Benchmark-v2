def remove_repeat_chars(s):
    chars_to_remove = set(s[6:9])
    for char in chars_to_remove:
        if s[6:9].count(char) > 1:
            s = s.replace(char, '', s[6:9].index(char))
    return s