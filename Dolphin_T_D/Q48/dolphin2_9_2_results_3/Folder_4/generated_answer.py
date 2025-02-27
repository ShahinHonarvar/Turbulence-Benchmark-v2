def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    if all((i in t for i in range(a + 1, b))):
        return ''
    missing_nums = [i for i in range(a + 1, b) if i not in t]
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]