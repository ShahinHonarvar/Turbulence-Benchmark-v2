def remove_repeat_chars(s):
    repeated_chars = set([c for c in s[8:10] if s[8:10].count(c) > 1])
    return ''.join([c for c in s if c not in repeated_chars])