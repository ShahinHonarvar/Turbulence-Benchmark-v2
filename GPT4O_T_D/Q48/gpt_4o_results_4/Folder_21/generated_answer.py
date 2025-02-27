def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    numbers_in_range = set(t[16:57])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers_in_range))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]