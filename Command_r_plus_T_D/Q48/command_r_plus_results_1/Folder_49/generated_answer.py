def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[80], numbers[200])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(numbers[81:200])
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()