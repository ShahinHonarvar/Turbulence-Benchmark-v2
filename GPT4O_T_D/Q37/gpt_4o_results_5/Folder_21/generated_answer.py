def filter_chars(s):
    to_remove = set((c for c in s[603:760] if 'Q' <= c <= 'h'))
    return ''.join((c for c in s if c not in to_remove))