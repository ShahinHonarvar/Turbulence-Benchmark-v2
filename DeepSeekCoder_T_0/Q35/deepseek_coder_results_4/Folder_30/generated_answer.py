def remove_repeat_chars(s):
    to_remove = set()
    for i in range(23, 24):
        if s[i] in s[:i] + s[i + 1:] and s[i] not in to_remove:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result