def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[33], numbers[78])
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum(numbers[34:78])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]