def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[60], numbers[90])
    range_sum = 0
    range_numbers = set(numbers[61:91])
    for num in range(a + 1, b):
        if num not in range_numbers:
            range_sum += num
    if range_sum:
        return bin(range_sum)[2:] if range_sum % 2 else hex(range_sum)[2:].upper()
    else:
        return ''