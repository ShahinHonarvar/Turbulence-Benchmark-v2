def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in t[111:348]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]