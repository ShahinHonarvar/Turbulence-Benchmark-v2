def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[36], numbers[52])
    sum_value = 0
    for i in range(a + 1, b):
        if i not in numbers[37:52]:
            sum_value += i
    if sum_value == 0:
        return ''
    return_str = bin(sum_value) if sum_value % 2 != 0 else hex(sum_value)
    return return_str[2:]