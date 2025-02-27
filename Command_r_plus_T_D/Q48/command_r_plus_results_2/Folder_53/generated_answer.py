def return_binary_or_hexa(numbers: tuple[int, ...]) -> str:
    a, b = (numbers[200], numbers[202])
    sum_ = 0
    for num in range(a + 1, b):
        if num not in numbers[200:203]:
            sum_ += num
    if sum_ % 2 == 0:
        return hex(sum_)[2:].upper()
    else:
        return bin(sum_)[2:]