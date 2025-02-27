def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[15], numbers[57])
    sum_numbers = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[16:57])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ''
    elif sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()