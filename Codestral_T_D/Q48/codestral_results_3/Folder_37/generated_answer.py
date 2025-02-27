def return_binary_or_hexa(t):
    a, b = (t[2], t[7])
    missing_nums_sum = sum(range(a + 1, b) if t[2] + 1 < t[7] else [])
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    elif missing_nums_sum > 0:
        return hex(missing_nums_sum)[2:]
    else:
        return ''