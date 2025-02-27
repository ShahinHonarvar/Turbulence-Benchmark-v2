def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[50], numbers[200])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[51:200]))
    if sum_numbers in numbers[51:200]:
        return ''
    return bin(sum_numbers)[2:] if sum_numbers % 2 != 0 else hex(sum_numbers)[2:].upper()