def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[57], numbers[85])
    sum_range = sum((i for i in range(a + 1, b) if i not in numbers[57:85]))
    return bin(sum_range)[2:] if sum_range % 2 else hex(sum_range)[2:].upper()