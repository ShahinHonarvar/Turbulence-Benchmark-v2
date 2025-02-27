def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[19], numbers[32])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[19:32]:
            range_sum += i
    if range_sum == 0:
        return ''
    return_str = bin(range_sum) if range_sum % 2 != 0 else hex(range_sum)
    return return_str[2:]