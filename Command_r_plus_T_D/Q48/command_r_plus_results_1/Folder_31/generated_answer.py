def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[33], numbers[78])
    sum_range = sum((i for i in range(a + 1, b) if i not in numbers[34:78]))
    if sum_range % 2 == 0:
        return hex(sum_range)[2:]
    else:
        return bin(sum_range)[2:]