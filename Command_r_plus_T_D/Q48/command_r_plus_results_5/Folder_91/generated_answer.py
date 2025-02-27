def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[6])
    sum_value = 0
    for num in range(a + 1, b):
        if num not in numbers[1:7]:
            sum_value += num
    if sum_value == 0:
        return ''
    return bin(sum_value)[2:] if sum_value % 2 != 0 else hex(sum_value)[2:].upper()