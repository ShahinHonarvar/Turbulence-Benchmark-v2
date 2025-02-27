def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[34], numbers[69])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[35:69]))
    if sum_numbers in numbers[35:69]:
        return ''
    return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()