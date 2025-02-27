def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[16], numbers[87])
    sum_values = sum(range(a + 1, b))
    for i in range(17, 87):
        if a + 1 <= numbers[i] <= b - 1:
            sum_values -= numbers[i]
    if sum_values:
        return bin(sum_values)[2:] if sum_values % 2 else hex(sum_values)[2:].upper()
    else:
        return ''