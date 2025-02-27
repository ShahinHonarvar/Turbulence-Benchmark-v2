def return_binary_or_hexa(t):
    a, b = (t[57], t[84])
    sum_of_missing = sum(set(range(a + 1, b)) - set(t[57:85]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()