def filter_chars(s):

    def char_in_range(c):
        return 52 <= s.index(c) <= 81 and 'A' <= c <= 'U'
    chars_to_remove = set((c for c in s if char_in_range(c)))
    return ''.join((c for c in s if c not in chars_to_remove))