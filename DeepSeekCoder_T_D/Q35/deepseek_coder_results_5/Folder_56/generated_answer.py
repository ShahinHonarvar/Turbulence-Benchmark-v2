def remove_repeat_chars(s):
    if len(s) < 10:
        return s
    to_remove = set()
    for i in range(8, 9):
        if s[i] in s[7:i] + s[i + 1:10]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result