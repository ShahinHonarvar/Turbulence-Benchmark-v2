def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    missing = set(range(a + 1, b)) - set(t[1:5])
    if not missing:
        return ''
    sum_val = sum(missing)
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()