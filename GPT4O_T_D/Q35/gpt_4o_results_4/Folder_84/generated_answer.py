def remove_repeat_chars(s):
    if len(s) <= 32:
        return s
    sub_str = s[33:44]
    repeated_chars = {c for c in sub_str if sub_str.count(c) > 1}
    return ''.join((c for c in s if c not in repeated_chars))