def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a = numbers[68]
    b = numbers[99]
    sum_range = sum(range(a + 1, b))
    missing_sum = sum_range - sum((numbers[i] for i in range(69, 99)))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()