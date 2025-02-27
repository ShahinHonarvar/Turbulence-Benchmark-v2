def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[110], numbers[348])
    sum_nums = 0
    for i in range(a + 1, b):
        if i not in numbers[110:349]:
            sum_nums += i
    if sum_nums:
        return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()
    return ''