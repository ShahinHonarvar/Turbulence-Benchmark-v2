def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[7], numbers[9])
    sum_numbers = sum(range(a + 1, b))
    range_numbers = set(numbers[8:10])
    if sum_numbers not in range_numbers:
        if sum_numbers % 2 == 0:
            return hex(sum_numbers)[2:]
        else:
            return bin(sum_numbers)[2:]
    else:
        return ''