def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    sum_missing = sum((num for num in range(a + 1, b) if num not in numbers[61:90]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]