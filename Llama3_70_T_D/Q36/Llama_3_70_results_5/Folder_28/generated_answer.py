def filter_chars(s):
    chars_to_remove = set((c for c in s[31:73] if 'M' < c < 'j'))
    return ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or i < 31 or i >= 73))