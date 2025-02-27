def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[10])
    sum_nums = sum(range(a + 1, b))
    for num in numbers[1:10]:
        if a + 1 <= num <= b - 1:
            sum_nums -= num
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()