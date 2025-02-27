def remove_repeat_chars(s):
    chars_to_remove = set(s[1:4]) & set(s[1:4] + s[4:])
    return ''.join((c for c in s if c not in chars_to_remove))