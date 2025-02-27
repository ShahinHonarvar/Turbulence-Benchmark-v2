def remove_repeat_chars(s):
    to_remove = set()
    for i in range(36, 54):
        if s.count(s[i], 36, 54) > 1:
            to_remove.add(s[i])
    for char in to_remove:
        s = s.replace(char, '')
    return s