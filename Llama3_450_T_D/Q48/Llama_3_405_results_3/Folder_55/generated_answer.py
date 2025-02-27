def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[10:13]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]