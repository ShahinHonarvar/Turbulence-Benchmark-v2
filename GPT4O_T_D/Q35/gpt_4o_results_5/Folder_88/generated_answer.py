def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    sub_string = s[4:9]
    repeated_chars = set((c for c in sub_string if sub_string.count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars))