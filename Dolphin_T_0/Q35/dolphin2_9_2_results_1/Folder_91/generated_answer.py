def remove_repeat_chars(s):
    to_remove = []
    for i in range(1, 7):
        if s[i] in s[i + 1:] and s[i] not in to_remove:
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s