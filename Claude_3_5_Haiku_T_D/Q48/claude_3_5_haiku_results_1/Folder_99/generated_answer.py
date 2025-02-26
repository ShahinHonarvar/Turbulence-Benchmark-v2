def return_binary_or_hexa(tup):
    a = tup[427]
    b = tup[669]
    missing_numbers = set(range(a + 1, b)) - set(tup[427:670])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]