def filter_chars(a):
    return ''.join([c for c in a if ord(c) not in range(32, 47) or ord(c) > 107])