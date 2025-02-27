def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    sum_range = set(range(a + 1, b))
    for number in numbers[13:92]:
        sum_range.discard(number)
    sum_ = sum(sum_range)
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]