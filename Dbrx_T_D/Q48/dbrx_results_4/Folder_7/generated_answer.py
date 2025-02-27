def return_binary_or_hexa(t):
    a, b = (t[10], t[97])
    sum_val = sum((x for x in range(a + 1, b) if x not in t[10:98]))
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()