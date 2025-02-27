def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[50], numbers[200])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(numbers[50:201])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'X')