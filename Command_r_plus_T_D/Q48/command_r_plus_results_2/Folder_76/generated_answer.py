def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[450], numbers[905])
    sum_nums = sum(range(a + 1, b))
    if sum_nums in numbers[450:906]:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()