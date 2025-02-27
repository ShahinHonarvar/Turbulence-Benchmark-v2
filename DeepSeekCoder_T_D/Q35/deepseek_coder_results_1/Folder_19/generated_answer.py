def remove_repeat_chars(s):
    repeat_chars = set(s[1:4]) & set(s)
    return ''.join((c for c in s if c not in repeat_chars))