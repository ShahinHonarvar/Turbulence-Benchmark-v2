def filter_chars(s):
    exclude = set((c for i, c in enumerate(s) if 164 <= i <= 706 and 'O' <= c <= '}'))
    return ''.join((c for c in s if c not in exclude))