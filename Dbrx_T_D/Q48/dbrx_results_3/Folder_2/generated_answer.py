def return_binary_or_hexa(input_tuple):
    if not all((isinstance(i, int) and i >= 0 for i in input_tuple)):
        raise ValueError('All tuple elements must be distinct nonnegative integers.')
    if len(input_tuple) < 94 or len(set(input_tuple[72:94])) != 22:
        return ''
    a, b = (input_tuple[72], input_tuple[93])
    missing_sum = sum((i for i in range(a + 1, b) if i not in input_tuple[72:93]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()