def remove_repeat_chars(s):
    to_remove = set()
    for i in range(330, 543):
        if s[i] in s[:i]:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))