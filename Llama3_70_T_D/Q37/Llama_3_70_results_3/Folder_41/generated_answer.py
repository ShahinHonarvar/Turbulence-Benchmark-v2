def filter_chars(s):

    def check_char(c):
        return ord(c) < 26 or ord(c) > 64 or c < 'V' or (c > 'o')
    return ''.join((c for c in s if check_char(c)))