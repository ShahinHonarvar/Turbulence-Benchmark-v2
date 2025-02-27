def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[-1]
    s = sum(set(range(a + 1, b)) - set(tup[1:-1]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]