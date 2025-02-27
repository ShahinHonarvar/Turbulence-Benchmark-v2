def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[20], numbers[36])
    range_sum = sum((i for i in range(a + 1, b) if i not in numbers[20:36]))
    return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()