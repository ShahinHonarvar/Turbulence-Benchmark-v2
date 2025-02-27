def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, len(s) if len(s) < 4 else 4):
        if s[i] in s[1:i] + s[i + 1:4]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result