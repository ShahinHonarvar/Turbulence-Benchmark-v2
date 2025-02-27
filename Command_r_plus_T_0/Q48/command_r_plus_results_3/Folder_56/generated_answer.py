def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[7], numbers[9])
    range_sum = sum(range(a + 1, b))
    range_set = set(numbers[8:10])
    if range_sum in range_set:
        return ''
    else:
        range_sum -= a + b
        if range_sum % 2 == 1:
            return bin(range_sum)[2:]
        else:
            return hex(range_sum)[2:].upper()