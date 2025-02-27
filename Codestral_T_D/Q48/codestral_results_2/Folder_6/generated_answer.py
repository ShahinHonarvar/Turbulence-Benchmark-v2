def return_binary_or_hexa(t):
    a, b = (t[20], t[93])
    missing_sum = sum(range(a + 1, b)) - sum(t[20 + 1:93])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]