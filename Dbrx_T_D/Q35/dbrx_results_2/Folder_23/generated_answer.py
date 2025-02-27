def remove_repeat_chars(s):
    chars_between_20_36 = set(s[20:36])
    for char in chars_between_20_36:
        if s[20:36].count(char) > 1:
            s = s.replace(char, '', s[20:36].index(char))
    return s