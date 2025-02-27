def return_binary_or_hexa(sorted_tuple):
    a, b = (sorted_tuple[0], sorted_tuple[3])
    missing_numbers = set(range(a + 1, b)) - set(sorted_tuple[1:3])
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()