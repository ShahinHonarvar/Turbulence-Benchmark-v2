def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[6])
    sum_val = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_val += i
    if sum_val == 0:
        return ''
    return bin(sum_val)[2:] if sum_val % 2 != 0 else hex(sum_val)[2:].upper()