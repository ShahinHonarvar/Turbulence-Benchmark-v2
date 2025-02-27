def return_binary_or_hexa(t):
    a, b = (t[38], t[81])
    range_set = set(range(a + 1, b))
    missing_sum = sum(range_set - set(t[38:82]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]