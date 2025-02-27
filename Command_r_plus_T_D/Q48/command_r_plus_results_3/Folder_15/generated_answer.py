def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[4])
    sum_nums = sum(range(a + 1, b))
    for num in range(a + 1, b):
        if num in numbers[1:5]:
            sum_nums -= num
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()