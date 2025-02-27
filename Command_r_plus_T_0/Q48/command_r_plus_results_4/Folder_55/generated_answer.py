def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[10], numbers[12])
    sum_range = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:13])
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()