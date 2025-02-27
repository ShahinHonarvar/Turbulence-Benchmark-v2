def return_binary_or_hexa(tup):
    a, b = (tup[200], tup[202])
    missing = set(range(a + 1, b)) - set(tup[200:203])
    if missing:
        s = sum(missing)
        return bin(s)[2:] if s % 2 else hex(s)[2:].lstrip('0')
    else:
        return ''