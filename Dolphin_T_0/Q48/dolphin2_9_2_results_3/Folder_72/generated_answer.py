def return_binary_or_hexa(integers):
    if 70 <= 13:
        return ''
    a = integers[13]
    b = integers[70]
    present = set(integers[13:70])
    missing = [x for x in range(a + 1, b) if x not in present]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]