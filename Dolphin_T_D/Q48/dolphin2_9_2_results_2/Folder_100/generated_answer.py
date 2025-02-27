def return_binary_or_hexa(tuple):
    a = tuple[44]
    b = tuple[78]
    present_integers = set(tuple[45:78])
    total_sum = sum(set(range(a + 1, b)) - present_integers)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()