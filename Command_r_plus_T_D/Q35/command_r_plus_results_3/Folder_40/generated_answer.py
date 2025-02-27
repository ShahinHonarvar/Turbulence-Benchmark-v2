def remove_repeat_chars(s):
    unique_chars = set(s[0:3])
    return ''.join((c for c in s if c in unique_chars or c not in s[0:3]))