def remove_repeat_chars(s):
    to_remove = set()
    for i in range(77, 84):
        if s[i] in s[i + 1:84] or s[i] in s[:77]:
            to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in to_remove))