def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[450], numbers[905])
    sum_range = sum(range(a + 1, b))
    if sum_range in numbers[450:906]:
        return ''
    elif sum_range % 2 == 0:
        return hex(sum_range)[2:]
    else:
        return bin(sum_range)[2:]