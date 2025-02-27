def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[933], numbers[996])
    sum_range = sum(range(a + 1, b))
    if sum_range in numbers[934:996]:
        return ''
    else:
        return bin(sum_range)[2:] if sum_range % 2 != 0 else hex(sum_range)[2:].upper()