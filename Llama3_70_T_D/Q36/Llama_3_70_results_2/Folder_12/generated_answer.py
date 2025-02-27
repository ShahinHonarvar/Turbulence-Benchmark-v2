def filter_chars(s):

    def check_char(c):
        return ord(c) < 32 or ord(c) > 84 or (not 'm' < c < 'w')
    return ''.join((c for i, c in enumerate(s) if check_char(c) or i < 32 or i >= 84))