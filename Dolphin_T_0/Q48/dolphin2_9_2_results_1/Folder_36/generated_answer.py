def return_binary_or_hexa(tuple_):
    a = tuple_[110]
    b = tuple_[348]
    total = sum(range(a + 1, b))
    present = sum(tuple_[110:349])
    missing = total - present
    if missing == 0:
        return ''
    elif missing % 2:
        return bin(missing)[2:]
    else:
        return hex(missing)[2:]