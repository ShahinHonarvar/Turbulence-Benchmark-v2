def filter_chars(s):

    def is_valid(c):
        return 36 <= ord(c) <= 79 and '2' <= c <= 's'
    chars_to_remove = set((c for i, c in enumerate(s[:80]) if is_valid(c)))
    return ''.join((c for c in s if c not in chars_to_remove))