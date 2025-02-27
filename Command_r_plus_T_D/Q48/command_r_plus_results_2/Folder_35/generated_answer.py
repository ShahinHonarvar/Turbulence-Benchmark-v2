def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[77], numbers[84])
    sum_values = sum(range(a + 1, b))
    for i in range(78, 84):
        if numbers[i] in range(a + 1, b):
            sum_values -= numbers[i]
    if sum_values == 0:
        return ''
    return bin(sum_values)[2:] if sum_values % 2 != 0 else hex(sum_values)[2:].upper()