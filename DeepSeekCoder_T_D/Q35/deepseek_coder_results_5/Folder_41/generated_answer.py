def remove_repeat_chars(s):
    to_remove = set()
    for i in range(4, 8):
        if s[i] in s[4:i] or s[i] in s[i + 1:8]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result