def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[1:7]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]