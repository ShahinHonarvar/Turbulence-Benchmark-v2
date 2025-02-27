def filter_chars(a):
    return ''.join([ch for ch in a if ch < 'b' or ch > '*'] not in a[42:98])