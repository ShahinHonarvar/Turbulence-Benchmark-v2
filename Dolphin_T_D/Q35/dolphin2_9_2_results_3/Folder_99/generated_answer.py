def remove_repeat_chars(s):
    unique_chars = set(s[450:905])
    for char in unique_chars:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s