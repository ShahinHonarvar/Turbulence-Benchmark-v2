def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[22:25]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]