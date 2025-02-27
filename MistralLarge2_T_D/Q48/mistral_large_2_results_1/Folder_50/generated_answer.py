def return_binary_or_hexa(t):
    a, b = (t[13], t[76])
    nums_in_range = set(t[13:77])
    sum_missing = sum((i for i in range(a + 1, b) if i not in nums_in_range))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]