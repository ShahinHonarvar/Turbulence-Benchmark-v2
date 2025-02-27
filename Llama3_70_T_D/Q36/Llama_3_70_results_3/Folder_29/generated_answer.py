def filter_chars(s):

    def is_invalid_char(c):
        return 'H' < c < 's'

    def filter_char(s, c):
        return s.replace(c, '')
    s = s[:46] + s[68:]
    for c in set(s[46:68]):
        if is_invalid_char(c):
            s = filter_char(s, c)
    return s + s[68:]