def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers[8:10]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]