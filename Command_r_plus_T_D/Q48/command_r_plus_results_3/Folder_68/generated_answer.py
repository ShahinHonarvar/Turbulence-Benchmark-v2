def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[9])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers))
    if sum_numbers in numbers:
        return ''
    return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()