def return_binary_or_hexa(t):
    a, b = (t[1], t[7])
    non_present = set(range(a + 1, b)).difference(t[1:7])
    if not non_present:
        return ''
    sum_val = sum(non_present)
    if sum_val % 2:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()