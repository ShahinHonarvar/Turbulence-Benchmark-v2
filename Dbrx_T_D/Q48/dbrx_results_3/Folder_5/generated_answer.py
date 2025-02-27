def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    sum_range = set(range(a + 1, b))
    present_numbers = set(t[2:9])
    missing_numbers = sum_range - present_numbers
    if not missing_numbers:
        return ''
    sum_value = sum(missing_numbers)
    return bin(sum_value)[2:] if sum_value % 2 else hex(sum_value)[2:].upper()