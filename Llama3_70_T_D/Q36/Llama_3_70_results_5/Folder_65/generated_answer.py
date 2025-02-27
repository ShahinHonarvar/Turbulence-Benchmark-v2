def filter_chars(s):

    def func(c):
        return c <= 'F' or c >= 'O' or (not 58 <= ord(c) <= 82)
    return ''.join(filter(func, s))