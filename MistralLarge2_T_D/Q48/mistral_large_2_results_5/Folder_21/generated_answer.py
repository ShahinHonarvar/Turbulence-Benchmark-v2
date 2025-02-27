def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    range_set = set(t[15:58])
    missing_sum = sum((x for x in range(a + 1, b) if x not in range_set))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()