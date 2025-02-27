def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    numbers_in_range = set(numbers[1:9])
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers_in_range))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]