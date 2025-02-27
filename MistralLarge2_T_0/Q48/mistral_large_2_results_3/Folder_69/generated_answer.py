def return_binary_or_hexa(t):
    a, b = (t[39], t[43])
    missing_sum = sum(set(range(a + 1, b)) - set(t[39:44]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]