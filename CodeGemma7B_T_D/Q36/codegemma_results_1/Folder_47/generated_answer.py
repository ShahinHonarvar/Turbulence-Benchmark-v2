def filter_chars(str):
    return ''.join((c for c in str if ord(c) not in range(45, 57) or (ord(c) > ord('F') and ord(c) < ord('n'))))