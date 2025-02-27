def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[6], numbers[7])
    sum_nums = sum((i for i in range(a + 1, b) if i not in numbers[6:8]))
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()