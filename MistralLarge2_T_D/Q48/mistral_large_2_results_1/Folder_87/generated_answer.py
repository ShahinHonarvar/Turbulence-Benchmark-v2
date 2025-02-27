def return_binary_or_hexa(t):
    a, b = (t[20], t[43])
    present_numbers = set(t[20:44])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()