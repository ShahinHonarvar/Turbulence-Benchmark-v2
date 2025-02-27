def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    present = set(tup[81:86 + 1])
    all_num = set(range(a + 1, b))
    missing = all_num - present
    sum_of_missing = sum(missing)
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:].upper()
    else:
        return bin(sum_of_missing)[2:]
    if not missing:
        return ''