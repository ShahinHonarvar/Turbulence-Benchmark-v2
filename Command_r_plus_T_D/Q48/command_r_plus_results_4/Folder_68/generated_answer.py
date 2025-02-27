def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[9])
    sum_missing = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_missing += i
    if sum_missing:
        return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:].upper()
    return ''