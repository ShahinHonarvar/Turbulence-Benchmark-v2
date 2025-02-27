def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[2], numbers[5])
    range_sum = sum(range(a + 1, b))
    range_set = set(numbers[2:6])
    missing_sum = sum((i for i in range(a + 1, b) if i not in range_set))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:].upper()