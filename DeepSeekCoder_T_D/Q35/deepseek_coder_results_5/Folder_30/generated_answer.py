def remove_repeat_chars(s):
    to_remove = set()
    for i in range(22, 24):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result