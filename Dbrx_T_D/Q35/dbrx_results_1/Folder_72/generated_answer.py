def remove_repeat_chars(s):
    chars = set(s[12:70])
    for char in chars:
        if s[12:70].count(char) > 1:
            s = s.replace(char, '', s[12:70].index(char) + 12)
    return s