def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[2])
    sum_nums = sum(range(a + 1, b))
    for num in numbers[1:3]:
        if a < num < b:
            sum_nums -= num
    if sum_nums:
        return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()
    else:
        return ''