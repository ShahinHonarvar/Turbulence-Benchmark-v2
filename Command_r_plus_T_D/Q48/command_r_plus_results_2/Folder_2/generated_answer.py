def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[72], numbers[93])
    sum_numbers = sum(range(a + 1, b))
    for num in range(a + 1, b):
        if num in numbers[73:93]:
            sum_numbers -= num
    if sum_numbers == 0:
        return ''
    elif sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:]
    else:
        return format(sum_numbers, 'b')