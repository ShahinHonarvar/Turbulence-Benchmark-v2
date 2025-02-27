def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[60], numbers[200])
    sum_value = 0
    for i in range(a + 1, b):
        if i not in numbers[60:201]:
            sum_value += i
    if sum_value == 0:
        return ''
    return bin(sum_value)[2:] if sum_value % 2 != 0 else hex(sum_value)[2:].upper()