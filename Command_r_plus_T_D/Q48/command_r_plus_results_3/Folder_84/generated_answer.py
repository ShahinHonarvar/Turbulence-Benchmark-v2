def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[32], numbers[44])
    sum_range = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[33:44]]
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()