def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[19], numbers[32])
    sum_value = 0
    for i in range(a + 1, b):
        if i not in numbers[19:32]:
            sum_value += i
    if sum_value == 0:
        return ''
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].upper()