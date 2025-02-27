def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[99]
    missing = [i for i in range(a + 1, b) if i not in tup[86:100]]
    if missing:
        s = sum(missing)
        return bin(s)[2:] if s % 2 else hex(s)[2:].upper()
    else:
        return ''