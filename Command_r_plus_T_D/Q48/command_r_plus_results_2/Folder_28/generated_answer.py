def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[86], numbers[99])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(numbers[86:100])
    if missing_sum == 0:
        return ''
    binary_str = bin(missing_sum)[2:]
    hex_str = hex(missing_sum)[2:].upper()
    return binary_str if missing_sum % 2 != 0 else hex_str