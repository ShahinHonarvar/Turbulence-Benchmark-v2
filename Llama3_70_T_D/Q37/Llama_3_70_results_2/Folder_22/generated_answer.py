def filter_chars(s):

    def filter_func(c):
        return ord(c) < 33 or ord(c) > 70 or c < '7' or (c > 'k')
    return ''.join((c for c in s if filter_func(c)))