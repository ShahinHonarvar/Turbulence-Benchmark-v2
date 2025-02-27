def filter_chars(s):
    return ''.join([i for i in s if not (i in s[72:95] and '.' <= i <= 'b')])