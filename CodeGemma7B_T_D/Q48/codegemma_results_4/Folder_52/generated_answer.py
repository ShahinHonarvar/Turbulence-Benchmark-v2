def return_binary_or_hexa(t):
    a, b = (t[38], t[81])
    sum_missing = sum(set(range(a + 1, b)) - set(t[38:82]))
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:].upper()