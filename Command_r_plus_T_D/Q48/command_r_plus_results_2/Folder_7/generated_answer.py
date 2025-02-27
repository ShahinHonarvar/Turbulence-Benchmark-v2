def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[10], numbers[97])
    sum_range = sum(range(a + 1, b))
    if sum_range in numbers[11:97]:
        return ''
    return bin(sum_range)[2:] if sum_range % 2 != 0 else hex(sum_range)[2:].upper()