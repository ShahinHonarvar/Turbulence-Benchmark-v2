def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    present_numbers = set(t[15:58])
    sum_missing = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]