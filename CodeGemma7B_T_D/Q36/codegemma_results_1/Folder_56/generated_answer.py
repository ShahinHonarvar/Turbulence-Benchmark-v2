def filter_chars(str):
    return ''.join([i for i in str if ord(i) not in range(32, 51) or (ord(i) > ord('/') and ord(i) < ord('J'))])