def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    present = set(t[933:996])
    total = set(range(a + 1, b))
    missing = total.difference(present)
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]