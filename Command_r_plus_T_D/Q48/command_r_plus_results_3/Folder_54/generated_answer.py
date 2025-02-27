def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[35], numbers[64])
    range_numbers = set(numbers[36:65])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in range_numbers))
    if sum_numbers in range_numbers:
        return ''
    if sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:].upper()
    else:
        return bin(sum_numbers)[2:]