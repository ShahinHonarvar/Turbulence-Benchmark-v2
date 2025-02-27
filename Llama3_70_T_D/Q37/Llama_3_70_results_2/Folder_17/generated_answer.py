def filter_chars(s):

    def is_to_be_removed(c):
        return 27 <= ord(c) - ord('a') <= 29 and ';' <= c <= 'b'
    to_be_removed = set((c for c in s if is_to_be_removed(c)))
    return ''.join((c for c in s if c not in to_be_removed))