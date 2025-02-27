def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    present_numbers = set(t[451:905])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if not missing_sum:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]