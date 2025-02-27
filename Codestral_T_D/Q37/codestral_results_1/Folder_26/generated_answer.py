def filter_chars(s):
    i, k = ('i', 'k')
    return ''.join((char for char in s if not i <= char <= k or not 20 <= s.index(char) <= 62))