def return_binary_or_hexa(input_tuple):
    if not isinstance(input_tuple, tuple) or len(input_tuple) < 89 or (not all((isinstance(i, int) and i >= 0 for i in input_tuple))):
        return ''
    a, b = (input_tuple[56], input_tuple[88])
    if b <= a + 1:
        return ''
    sum_of_missing = sum(set(range(a + 1, b)) - set(input_tuple[56:89]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()