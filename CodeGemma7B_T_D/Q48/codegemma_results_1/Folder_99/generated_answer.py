def return_binary_or_hexa(a_and_b):
    a, b = a_and_b
    range_ints = set(range(a + 1, b))
    present_ints = set(a_and_b[427:669])
    missing_ints = range_ints - present_ints
    missing_sum = sum(missing_ints)
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()