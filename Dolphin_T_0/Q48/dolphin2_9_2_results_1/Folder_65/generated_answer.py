def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    if a != b - 1:
        missing = [num for num in range(a + 1, b) if num not in numbers[51:76]]
        sum_ = sum(missing)
        if sum_ % 2 == 1:
            return bin(sum_)[2:]
        else:
            return hex(sum_)[2:]
    else:
        return ''