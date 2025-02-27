def return_binary_or_hexa(t):
    a, b = (t[13], t[35])
    missing = set(range(a + 1, b))
    present = set(t[14:35])
    missing_sum = sum(missing - present)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''