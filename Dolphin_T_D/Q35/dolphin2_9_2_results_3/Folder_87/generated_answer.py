def remove_repeat_chars(s):
    to_remove = []
    for i in range(20, 43):
        if s.count(s[i]) > 1:
            to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s