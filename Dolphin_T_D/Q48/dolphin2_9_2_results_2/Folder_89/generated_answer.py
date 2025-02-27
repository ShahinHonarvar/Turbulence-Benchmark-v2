def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    present = set(numbers[55:85])
    sum_ = 0
    for num in range(a + 1, b):
        if num not in present:
            sum_ += num
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]