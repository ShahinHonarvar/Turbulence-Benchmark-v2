def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[7], numbers[9])
    range_sum = sum((i for i in range(a + 1, b) if i not in numbers[7:10]))
    if range_sum in numbers[7:10]:
        return ''
    return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()