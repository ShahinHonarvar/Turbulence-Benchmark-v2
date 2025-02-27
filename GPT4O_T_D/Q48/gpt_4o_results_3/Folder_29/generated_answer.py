def return_binary_or_hexa(t):
    a = t[70]
    b = t[98]
    missing_nums_sum = sum((x for x in range(a + 1, b) if x not in t[71:99]))
    if not missing_nums_sum:
        return ''
    if missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:]
    else:
        return bin(missing_nums_sum)[2:]