def remove_repeat_chars(s):
    target_chars = set(s[1:2])
    to_remove = {c for c in target_chars if s[1:2].count(c) > 1}
    return ''.join((c for c in s if c not in to_remove))