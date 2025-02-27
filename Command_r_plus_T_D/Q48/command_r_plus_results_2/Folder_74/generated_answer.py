def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[69], numbers[97])
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[69:97]))
    if sum_numbers in numbers[69:97]:
        return ''
    return bin(sum_numbers)[2:] if sum_numbers % 2 else hex(sum_numbers)[2:].upper()