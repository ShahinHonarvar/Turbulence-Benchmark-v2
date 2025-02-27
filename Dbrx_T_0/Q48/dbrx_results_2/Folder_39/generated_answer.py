def return_binary_or_hexa(t):
    a, b = (t[44], t[91])
    missing_numbers = set(range(a + 1, b)) - set(t[44:92])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()