def remove_repeat_chars(s):
    repeated_chars = {c for c in s[100:200] if s[100:200].count(c) > 1}
    return ''.join((c for c in s if c not in repeated_chars))