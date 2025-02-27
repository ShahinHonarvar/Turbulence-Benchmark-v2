def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    range_set = set(t[46:92])
    missing_sum = sum((x for x in range(a + 1, b) if x not in range_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]