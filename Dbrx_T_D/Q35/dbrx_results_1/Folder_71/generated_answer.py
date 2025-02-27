def remove_repeat_chars(s):
    chars_between = set(s[20:35])
    for char in chars_between:
        if s[20:35].count(char) > 1:
            s = s.replace(char, '', s[20:35].index(char))
    return s