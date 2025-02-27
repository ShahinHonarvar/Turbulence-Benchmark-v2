def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[0], numbers[2])
    sum_ = sum(range(a + 1, b))
    for num in numbers[1:3]:
        if a + 1 <= num <= b - 1:
            sum_ -= num
    if sum_ == 0:
        return ''
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:].upper()