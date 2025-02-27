def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[29], numbers[53])
    range_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[30:53]:
            range_sum += num
    if range_sum == 0:
        return ''
    return format(range_sum, 'b') if range_sum % 2 else format(range_sum, 'X')