def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[32], numbers[44])
    range_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[32:45]:
            range_sum += i
    if range_sum == 0:
        return ''
    return_str = bin(range_sum) if range_sum % 2 == 1 else hex(range_sum)
    return return_str[2:]