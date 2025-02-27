def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[86:91]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]