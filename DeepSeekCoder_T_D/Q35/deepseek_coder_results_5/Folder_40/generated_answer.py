def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    unique_chars = set(s[1:3])
    for char in unique_chars:
        if s[1:3].count(char) > 1:
            s = s.replace(char, '')
    return s