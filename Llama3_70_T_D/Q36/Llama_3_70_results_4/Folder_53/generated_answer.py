def filter_chars(s):

    def is_in_range(c):
        return 90 < ord(c) < 97 and 'j' < c < 'w'
    chars_to_remove = set((c for c in s if is_in_range(c)))
    return ''.join((c for c in s if c not in chars_to_remove))