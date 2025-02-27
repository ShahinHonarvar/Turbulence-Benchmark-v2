def filter_chars(s):
    return ''.join((i for i in s if i <= 't' and i >= 'R' and (s.index(i) not in range(8, 9))))