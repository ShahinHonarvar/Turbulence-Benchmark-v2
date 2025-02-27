def filter_chars(s):

    def should_remove(c):
        return 'l' < c < 't'
    to_remove = set((c for i, c in enumerate(s) if 283 < i < 484 and should_remove(c)))
    return ''.join((c for c in s if c not in to_remove))