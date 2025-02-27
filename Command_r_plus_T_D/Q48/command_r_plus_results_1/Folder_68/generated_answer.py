def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[9])
    sum_ = sum(range(a + 1, b))
    for i in range(1, 9):
        if numbers[i] in range(a + 1, b):
            sum_ -= numbers[i]
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:].upper()