def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[32], numbers[99])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in numbers[32:100]:
            sum_ += i
    if sum_ % 2 == 0:
        return hex(sum_)[2:].upper()
    else:
        return bin(sum_)[2:]