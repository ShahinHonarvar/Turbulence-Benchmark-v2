def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    numbers_in_range = set(t[4:8])
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers_in_range))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]