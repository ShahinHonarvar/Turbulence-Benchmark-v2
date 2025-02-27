def filter_chars(s):

    def condition(c):
        return 373 <= ord(c) <= 901 and 'T' <= c <= 'h'
    chars_to_remove = set((c for c in s if condition(c)))
    return ''.join((c for c in s if c not in chars_to_remove))