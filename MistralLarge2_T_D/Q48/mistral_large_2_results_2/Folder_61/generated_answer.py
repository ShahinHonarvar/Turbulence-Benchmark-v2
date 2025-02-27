def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    missing_sum = sum(set(range(a + 1, b)) - set(t[1:8]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()