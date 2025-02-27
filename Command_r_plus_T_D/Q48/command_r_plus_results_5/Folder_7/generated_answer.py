def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[10], numbers[97])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in numbers[10:97]:
            sum_val += i
    if sum_val == 0:
        return ''
    return hex(sum_val)[2:].upper() if sum_val % 2 == 0 else bin(sum_val)[2:]