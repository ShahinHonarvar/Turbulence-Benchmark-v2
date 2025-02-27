def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[37], numbers[43])
    sum_range = sum((i for i in range(a + 1, b) if i not in numbers[38:43]))
    if sum_range in numbers[38:43]:
        return ''
    else:
        return bin(sum_range)[2:] if sum_range % 2 != 0 else hex(sum_range)[2:].upper()