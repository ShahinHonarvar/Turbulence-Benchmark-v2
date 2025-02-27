def filter_chars(s):

    def filter_func(c):
        return c < 'V' or c > 'o'

    def filter_range(c):
        return ord(c) < 26 or ord(c) > 64

    def final_filter(c):
        return filter_func(c) or filter_range(c)
    return ''.join((c for c in s if final_filter(c)))