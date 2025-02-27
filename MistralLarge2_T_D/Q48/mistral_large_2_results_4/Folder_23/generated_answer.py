def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    missing_sum = sum(set(range(a + 1, b)) - set(t[20:37]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()