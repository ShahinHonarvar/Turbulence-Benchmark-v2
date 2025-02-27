def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, _, b = numbers
    sum_nums = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(numbers[1:3])
    if missing_nums:
        sum_missing = sum(missing_nums)
        if sum_missing % 2:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:].upper()
    return ''