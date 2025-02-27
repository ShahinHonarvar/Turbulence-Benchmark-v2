def filter_chars(s):
    chars_to_remove = [s[i] for i in range(37, 56) if s[i] >= '6' and s[i] <= '_']
    return ''.join((c for c in s if c not in chars_to_remove))