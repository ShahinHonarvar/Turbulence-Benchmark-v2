def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[42], numbers[87])
    sum_range = sum((i for i in range(a + 1, b) if i not in numbers[42:87]))
    if sum_range in numbers[42:87]:
        return ''
    elif sum_range % 2 == 0:
        return hex(sum_range)[2:].upper()
    else:
        return bin(sum_range)[2:]