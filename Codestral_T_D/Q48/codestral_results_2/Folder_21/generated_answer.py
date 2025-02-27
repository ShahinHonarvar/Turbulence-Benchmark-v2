def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    missing = [i for i in range(a + 1, b) if i not in tup[15 + 1:57]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]