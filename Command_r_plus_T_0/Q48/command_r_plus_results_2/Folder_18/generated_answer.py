def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[56], numbers[90])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in numbers[57:90]:
            sum_ += i
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:].upper()