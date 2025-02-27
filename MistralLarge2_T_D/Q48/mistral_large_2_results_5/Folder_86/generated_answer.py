def return_binary_or_hexa(t):
    a, b = (t[19], t[32])
    missing_sum = sum(set(range(a + 1, b)) - set(t[19:33]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]