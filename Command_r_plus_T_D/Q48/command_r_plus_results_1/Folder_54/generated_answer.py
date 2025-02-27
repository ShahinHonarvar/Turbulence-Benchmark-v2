def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[35], numbers[64])
    sum_value = 0
    for i in range(a + 1, b):
        if i not in numbers[36:65]:
            sum_value += i
    if sum_value:
        return bin(sum_value)[2:] if sum_value % 2 else hex(sum_value)[2:].upper()
    return ''