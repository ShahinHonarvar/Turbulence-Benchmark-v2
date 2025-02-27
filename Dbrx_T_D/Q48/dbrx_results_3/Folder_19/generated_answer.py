def return_binary_or_hexa(input_tuple):
    if len(input_tuple) != 5 or not all((isinstance(i, int) and i >= 0 for i in input_tuple)):
        return ''
    a, b = (input_tuple[1], input_tuple[4])
    if a >= b:
        return ''
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[1:4])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()