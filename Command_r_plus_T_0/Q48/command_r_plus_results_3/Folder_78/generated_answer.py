def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[62], numbers[96])
    range_sum = sum(range(a + 1, b))
    missing_sum = range_sum - sum(set(numbers[63:96]) - set(range(a + 1, b)))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()