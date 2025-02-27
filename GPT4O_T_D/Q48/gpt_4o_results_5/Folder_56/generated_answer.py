def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[8:9]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]