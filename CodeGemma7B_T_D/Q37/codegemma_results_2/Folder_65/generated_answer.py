def filter_chars(st):
    return ''.join((ch for ch in st if not (ch in st[61:71] and ch >= '0' and (ch <= '@'))))