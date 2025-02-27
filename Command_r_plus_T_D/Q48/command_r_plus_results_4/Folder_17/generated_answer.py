def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[73], numbers[84])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(numbers[74:84])
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]