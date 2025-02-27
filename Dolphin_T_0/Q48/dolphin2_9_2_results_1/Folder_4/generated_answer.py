def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    sum_val = sum(range(a + 1, b)) - sum(t[50:75])
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()