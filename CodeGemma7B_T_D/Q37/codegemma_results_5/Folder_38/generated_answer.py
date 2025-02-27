def filter_chars(string):

    def is_between_inclusive(i):
        return 24 <= i <= 79

    def is_in_range(c):
        return 'a' <= c <= 'f'
    return ''.join([c for c in string if not (is_between_inclusive(string.index(c)) and is_in_range(c))])