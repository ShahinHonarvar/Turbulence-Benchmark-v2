def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[97])
    if all((i in numbers for i in range(a + 1, b))):
        return ''
    sum_ = sum((i for i in range(a + 1, b) if i not in numbers))
    if sum_ % 2 == 0:
        return hex(sum_)[2:]
    else:
        return bin(sum_)[2:]