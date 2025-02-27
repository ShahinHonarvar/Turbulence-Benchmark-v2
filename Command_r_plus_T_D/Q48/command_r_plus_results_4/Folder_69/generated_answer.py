def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[39], numbers[43])
    sum_range = sum(range(a + 1, b))
    if sum_range in numbers[40:43]:
        return ''
    elif sum_range % 2 == 0:
        return hex(sum_range)[2:].upper()
    else:
        return bin(sum_range)[2:]