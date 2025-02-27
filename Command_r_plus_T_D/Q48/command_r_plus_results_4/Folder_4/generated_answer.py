def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[49], numbers[74])
    sum_range = sum(range(a + 1, b))
    for num in range(a + 1, b):
        if num in numbers[50:74]:
            sum_range -= num
    if sum_range == 0:
        return ''
    return bin(sum_range)[2:] if sum_range % 2 else hex(sum_range)[2:].upper()