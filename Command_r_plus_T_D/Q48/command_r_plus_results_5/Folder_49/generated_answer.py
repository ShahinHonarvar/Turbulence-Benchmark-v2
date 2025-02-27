def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[80], numbers[200])
    sum_nums = sum((i for i in range(a + 1, b) if i not in numbers[80:201]))
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()