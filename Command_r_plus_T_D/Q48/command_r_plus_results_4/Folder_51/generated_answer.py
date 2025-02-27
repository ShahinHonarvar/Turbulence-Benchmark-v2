def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[6], numbers[9])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[6:10]:
            range_sum += i
    if range_sum == 0:
        return ''
    return format(range_sum, 'x') if range_sum % 2 == 0 else format(range_sum, 'b')