def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    to_remove = {c for c in s[1:3] if s[1:3].count(c) > 1}
    return ''.join((c for c in s if c not in to_remove))