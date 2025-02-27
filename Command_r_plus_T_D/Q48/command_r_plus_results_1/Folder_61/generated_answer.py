def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[8])
    sum_nums = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)).difference(set(numbers[:9]))
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()