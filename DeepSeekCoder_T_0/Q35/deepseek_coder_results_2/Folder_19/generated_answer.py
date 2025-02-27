def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, len(s) - 1):
        if 1 < i < 4 and s[i] in s[1:i] + s[i + 1:4]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result