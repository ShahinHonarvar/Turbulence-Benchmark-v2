def remove_repeat_chars(s):
    chars_to_remove = set(s[38:81])
    for char in chars_to_remove:
        if s[38:81].count(char) > 1:
            s = s.replace(char, '', s[38:81].index(char))
    return s