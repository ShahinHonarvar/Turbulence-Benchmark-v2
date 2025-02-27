def filter_chars(s):

    def is_valid(c):
        return not 't' < c < 'x'
    return ''.join((c for i, c in enumerate(s) if i < 42 or i >= 68 or is_valid(c)))