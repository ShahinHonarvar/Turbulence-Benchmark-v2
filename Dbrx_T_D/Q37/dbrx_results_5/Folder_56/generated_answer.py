def filter_chars(input_string):

    def in_range(c):
        return 'K' <= c <= 'a'
    return ''.join((c for i, c in enumerate(input_string) if not (71 <= i < 94 and in_range(c))))