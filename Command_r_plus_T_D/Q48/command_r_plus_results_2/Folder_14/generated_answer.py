def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[2], numbers[5])
    sum_nums = sum(range(a + 1, b))
    for i in range(3, 6):
        if a + 1 <= numbers[i] <= b - 1:
            sum_nums -= numbers[i]
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()