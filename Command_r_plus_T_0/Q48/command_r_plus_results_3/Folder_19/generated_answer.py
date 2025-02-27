def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[1], numbers[4])
    range_sum = sum(range(a + 1, b))
    range_set = set(numbers[1:5])
    missing_sum = sum((i for i in range(a + 1, b) if i not in range_set))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()