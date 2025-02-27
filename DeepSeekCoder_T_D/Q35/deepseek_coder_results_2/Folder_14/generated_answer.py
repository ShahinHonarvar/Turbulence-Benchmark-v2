def remove_repeat_chars(s):
    to_remove = set()
    for i in range(2, len(s) - 2):
        if s[i] in s[i + 1:]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result