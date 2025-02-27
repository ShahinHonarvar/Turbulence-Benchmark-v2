def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[36:54]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 != 0:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]