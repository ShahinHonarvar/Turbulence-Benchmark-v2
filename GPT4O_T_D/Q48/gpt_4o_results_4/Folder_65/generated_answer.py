def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    sum_missing = sum((num for num in range(a + 1, b) if num not in numbers[52:76]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]