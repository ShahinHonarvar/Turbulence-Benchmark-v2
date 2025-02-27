def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    missing_numbers = set(range(a + 1, b)) - set(t[276:871])
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]