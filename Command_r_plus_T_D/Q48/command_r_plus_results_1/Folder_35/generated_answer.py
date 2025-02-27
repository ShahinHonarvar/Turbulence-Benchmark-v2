def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[77], numbers[84])
    range_sum = sum(range(a + 1, b))
    missing_sum = range_sum - sum(numbers[77:84])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()