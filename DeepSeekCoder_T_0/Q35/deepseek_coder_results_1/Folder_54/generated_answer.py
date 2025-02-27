def remove_repeat_chars(s):
    if len(s) <= 64:
        return s
    middle_chars = list(s[35:64])
    unique_chars = set(middle_chars)
    for char in unique_chars:
        if middle_chars.count(char) > 1:
            s = s.replace(char, '')
    return s