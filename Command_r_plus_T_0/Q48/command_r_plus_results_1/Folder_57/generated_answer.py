def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[25], numbers[80])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[26:80]:
            range_sum += i
    if range_sum == 0:
        return ''
    return format(range_sum, 'b') if range_sum % 2 else format(range_sum, 'X')