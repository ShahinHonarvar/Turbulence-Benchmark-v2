def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[44], numbers[91])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[45:91]))
    if sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:]
    else:
        return bin(sum_numbers)[2:]