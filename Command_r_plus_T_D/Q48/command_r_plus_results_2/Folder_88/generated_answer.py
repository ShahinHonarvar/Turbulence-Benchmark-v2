def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[3], numbers[9])
    sum_ = 0
    for num in range(a + 1, b):
        if num not in numbers[3:10]:
            sum_ += num
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 != 0 else hex(sum_)[2:].upper()