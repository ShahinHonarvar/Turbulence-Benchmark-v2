def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[56], numbers[90])
    sum_range = sum(range(a + 1, b))
    if sum_range in numbers[57:90]:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].upper()