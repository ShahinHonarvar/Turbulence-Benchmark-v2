def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    missing = set(range(a + 1, b))
    present = set(t[56 + 1:90])
    missing_in_range = missing - present
    total_sum = sum(missing_in_range)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]