def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[90], numbers[200])
    sum_range = sum((i for i in range(a + 1, b) if i not in numbers[91:200]))
    if sum_range in numbers[91:200]:
        return ''
    return bin(sum_range)[2:] if sum_range % 2 != 0 else hex(sum_range)[2:].upper()