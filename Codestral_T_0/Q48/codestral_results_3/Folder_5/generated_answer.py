def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    missing_sum = sum(range(a + 1, b)) - sum(t[2:8])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]