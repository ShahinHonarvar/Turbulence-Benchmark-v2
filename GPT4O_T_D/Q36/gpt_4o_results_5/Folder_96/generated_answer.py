def filter_chars(s):
    if len(s) <= 38:
        return s
    sub_str = s[38:81]
    chars_to_remove = set((c for c in sub_str if '.' < c < '^'))
    return ''.join((c for c in s if c not in chars_to_remove))