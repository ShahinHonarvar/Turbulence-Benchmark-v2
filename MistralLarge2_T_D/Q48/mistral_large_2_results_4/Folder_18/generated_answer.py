def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    missing_sum = sum(set(range(a + 1, b)) - set(t[56:91]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]