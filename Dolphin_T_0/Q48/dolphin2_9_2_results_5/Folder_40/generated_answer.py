def return_binary_or_hexa(t):
    a = t[0]
    b = t[3]
    missing = [x for x in range(a + 1, b) if x not in t]
    if not missing:
        return ''
    sum_val = sum(missing)
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]