def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    arr = t[10:77]
    sum_val = sum((i for i in range(a + 1, b) if i not in arr))
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]