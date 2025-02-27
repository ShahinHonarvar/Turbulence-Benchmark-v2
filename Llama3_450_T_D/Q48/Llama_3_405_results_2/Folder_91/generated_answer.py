def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[:7]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]