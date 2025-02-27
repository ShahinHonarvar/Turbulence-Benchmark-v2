def return_binary_or_hexa(t):
    a, b = (t[10], t[12])
    missing_sum = sum(set(range(a + 1, b)) - set(t[10:12]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]