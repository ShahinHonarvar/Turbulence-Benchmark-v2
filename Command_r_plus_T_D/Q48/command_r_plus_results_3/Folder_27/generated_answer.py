def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[86], numbers[89])
    sum_range = sum(range(a + 1, b))
    sum_diff = sum_range - sum(numbers[86:90])
    if sum_diff == 0:
        return ''
    if sum_diff % 2 == 1:
        return bin(sum_diff)[2:]
    return hex(sum_diff)[2:].upper()