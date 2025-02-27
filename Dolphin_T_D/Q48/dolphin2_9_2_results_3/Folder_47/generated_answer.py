def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    sum_ = sum(set(range(a + 1, b)) - set(numbers[30:53]))
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()