def remove_repeat_chars(s):
    unique_chars = set(s[0:2])
    return ''.join((c for c in s if c in unique_chars))