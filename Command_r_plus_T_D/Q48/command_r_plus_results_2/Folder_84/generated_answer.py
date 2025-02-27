def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[32], numbers[44])
    range_sum = sum((i for i in range(a + 1, b) if i not in numbers[32:45]))
    if range_sum % 2 == 0:
        return hex(range_sum)[2:].upper()
    else:
        return bin(range_sum)[2:]