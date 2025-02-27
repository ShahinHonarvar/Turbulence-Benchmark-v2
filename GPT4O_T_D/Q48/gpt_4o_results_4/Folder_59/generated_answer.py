def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[10]
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in numbers[0:11]))
    if sum_of_missing == 0:
        return ''
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]