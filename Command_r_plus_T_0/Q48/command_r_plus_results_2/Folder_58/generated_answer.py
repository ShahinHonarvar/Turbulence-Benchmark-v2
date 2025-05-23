def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[275], numbers[871])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(set(numbers[276:871]) & set(range(a + 1, b)))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:].upper()