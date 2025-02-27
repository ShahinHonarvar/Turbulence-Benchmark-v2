def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[1], numbers[7])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in numbers[1:8]:
            sum_ += i
    if sum_ == 0:
        return ''
    return hex(sum_)[2:].upper() if sum_ % 2 == 0 else bin(sum_)[2:]