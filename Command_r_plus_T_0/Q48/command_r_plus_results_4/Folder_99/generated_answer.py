def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[427], numbers[669])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(set(numbers[428:669]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()