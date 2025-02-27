def remove_repeat_chars(s):
    seen = {}
    to_remove = set()
    for i in range(63, 96):
        if s[i] in seen:
            to_remove.add(s[i])
        else:
            seen[s[i]] = 1
    return ''.join((c for c in s if c not in to_remove))