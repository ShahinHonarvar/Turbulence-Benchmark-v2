def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    present_numbers = set(t[21:43])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]