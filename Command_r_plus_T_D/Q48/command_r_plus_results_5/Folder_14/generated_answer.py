def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[2], numbers[5])
    sum_range = sum(range(a + 1, b))
    range_numbers = set(numbers[2:6])
    missing_sum = sum_range - sum(range_numbers)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()