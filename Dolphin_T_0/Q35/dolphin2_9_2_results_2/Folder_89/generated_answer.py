def remove_repeat_chars(s):
    to_remove = set()
    for i in range(55, 84):
        if s[i] in s[84:]:
            to_remove.add(s[i])
    return ''.join([c for c in s if c not in to_remove])