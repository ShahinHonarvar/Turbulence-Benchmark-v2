def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[10], numbers[12])
    sum_values = sum((i for i in range(a + 1, b) if i not in numbers[10:13]))
    if sum_values == 0:
        return ''
    elif sum_values % 2 == 1:
        return bin(sum_values)[2:]
    else:
        return hex(sum_values)[2:].upper()