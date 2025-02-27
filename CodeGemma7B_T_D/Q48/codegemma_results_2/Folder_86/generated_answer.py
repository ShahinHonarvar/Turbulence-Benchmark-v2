def return_binary_or_hexa(tup):
    a, b = (tup[19], tup[32])
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in tup[19:33]:
            sum_missing += i
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:].upper()