def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[30], numbers[200])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in numbers[30:201]:
            sum_ += i
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:].upper()