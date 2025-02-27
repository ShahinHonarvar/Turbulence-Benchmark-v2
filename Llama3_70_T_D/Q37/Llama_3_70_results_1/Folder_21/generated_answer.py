def filter_chars(s):

    def is_valid(c):
        return 603 <= ord(c) <= 759 and 'Q' <= c <= 'h'
    chars_to_remove = set((c for c in s if is_valid(c)))
    return ''.join((c for c in s if c not in chars_to_remove))