def return_binary_or_hexa(t):
    a, b = (t[27], t[96])
    missing_sum = sum(set(range(a + 1, b)) - set(t[27:97]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()