def return_binary_or_hexa(input_tuple):
    a = input_tuple[49]
    b = input_tuple[74]
    required_set = set(range(a + 1, b))
    existing_set = set(input_tuple[49:75])
    missing_set = required_set - existing_set
    if not missing_set:
        return ''
    sum_missing = sum(missing_set)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()