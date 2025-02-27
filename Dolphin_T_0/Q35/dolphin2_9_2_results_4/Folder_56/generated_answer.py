def remove_repeat_chars(s):
    to_remove = []
    for i in range(7, 10):
        for j in range(i + 1, 10):
            if s[i] == s[j]:
                to_remove.append(s[i])
    for c in to_remove:
        s = s.replace(c, '')
    return s