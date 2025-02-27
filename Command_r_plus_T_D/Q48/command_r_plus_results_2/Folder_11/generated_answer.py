def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[48], numbers[76])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[48:76]))
    if sum_numbers == 0:
        return ''
    elif sum_numbers % 2 == 1:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:].upper()