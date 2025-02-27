def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    present_numbers = set(t[38:82])
    missing_numbers = [x for x in range(a + 1, b) if x not in present_numbers]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]