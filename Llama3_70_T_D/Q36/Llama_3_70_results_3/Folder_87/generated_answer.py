def filter_chars(s):

    def filter_func(c):
        return not (32 < ord(c) < 61 and '3' < c < 'D')
    return ''.join(filter(filter_func, s))