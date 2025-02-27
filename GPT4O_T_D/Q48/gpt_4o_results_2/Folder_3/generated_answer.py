def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    numbers_in_range = set(t[57:88])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers_in_range))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]