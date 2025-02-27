def remove_repeat_chars(s):
    chars_to_remove = set(s[3:9])
    for char in chars_to_remove:
        if s[3:9].count(char) > 1:
            s = s.replace(char, '', s[3:9].index(char))
            s = s.replace(char, '', s[3:9].index(char, s[3:9].index(char) + 1))
    return s