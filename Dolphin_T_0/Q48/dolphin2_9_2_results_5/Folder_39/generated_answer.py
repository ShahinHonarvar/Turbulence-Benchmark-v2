def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    if b == a + 1:
        return ''
    sum_ = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]