def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[39], numbers[43])
    sum_range = sum((i for i in range(a + 1, b) if i not in numbers[39:43]))
    if sum_range in numbers[39:43]:
        return ''
    elif sum_range % 2 == 0:
        return hex(sum_range)[2:]
    else:
        return bin(sum_range)[2:]