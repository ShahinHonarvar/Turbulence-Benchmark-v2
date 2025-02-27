def filter_chars(s):

    def should_remove(c):
        return 31 <= ord(c) <= 38 and ';' <= c <= 'g'
    chars_to_remove = set((c for c in s if should_remove(c)))
    return ''.join((c for c in s if c not in chars_to_remove))