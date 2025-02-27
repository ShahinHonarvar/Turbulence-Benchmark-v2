def filter_chars(s):

    def should_remove(ch):
        return '#' < ch < 'L'
    to_remove = set(filter(should_remove, s[70:87]))
    return ''.join((c for c in s if c not in to_remove))