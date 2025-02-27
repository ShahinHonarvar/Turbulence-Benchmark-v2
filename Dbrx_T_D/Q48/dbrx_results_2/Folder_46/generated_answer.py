def return_binary_or_hexa(indices_tuple):
    if not isinstance(indices_tuple, tuple) or len(indices_tuple) != 2:
        raise ValueError('Input must be a tuple of length 2')
    if not isinstance(indices_tuple[0], int) or not indices_tuple[0] >= 0 or (not isinstance(indices_tuple[1], int)) or (not indices_tuple[1] >= indices_tuple[0]) or (not indices_tuple[1] - indices_tuple[0] >= 79 - 10):
        raise ValueError('Tuple elements must be distinct nonnegative integers with difference at least 69')
    a, b = indices_tuple
    a += 1
    b -= 1
    if a > b:
        return ''
    present_set = set(indices_tuple[10:80])
    missing_set = set(range(a, b + 1)) - present_set
    if not missing_set:
        return ''
    sum_of_missing = sum(missing_set)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]