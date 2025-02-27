def return_binary_or_hexa(tup):
    a, b = (tup[44], tup[91])
    present_numbers = set(tup[45:91])
    missing_numbers = set(range(a + 1, b)) - present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()