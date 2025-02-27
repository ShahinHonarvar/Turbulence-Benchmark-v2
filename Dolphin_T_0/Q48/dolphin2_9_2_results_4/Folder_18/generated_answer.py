def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    missing = [i for i in range(a + 1, b) if i not in t[56:90]]
    if missing:
        sum_val = sum(missing)
        if sum_val % 2:
            return bin(sum_val)[2:]
        else:
            return hex(sum_val)[2:]
    else:
        return ''