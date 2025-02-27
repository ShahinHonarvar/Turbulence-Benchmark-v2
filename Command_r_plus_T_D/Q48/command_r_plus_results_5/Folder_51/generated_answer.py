def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[6], numbers[9])
    range_sum = sum(range(a + 1, b))
    range_set = set(numbers[6:10])
    if range_sum not in range_set:
        if range_sum % 2 == 0:
            return hex(range_sum)[2:].upper()
        else:
            return bin(range_sum)[2:]
    else:
        return ''