def remove_repeat_chars(s):
    to_remove = set()
    for i in range(7, 9):
        c = s[i]
        if s.count(c, 7, 9) > 1:
            to_remove.add(c)
    result = []
    for c in s:
        if c not in to_remove:
            result.append(c)
    return ''.join(result)