def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[2], numbers[7])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in numbers[2:8]:
            sum_val += i
    if sum_val == 0:
        return ''
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()