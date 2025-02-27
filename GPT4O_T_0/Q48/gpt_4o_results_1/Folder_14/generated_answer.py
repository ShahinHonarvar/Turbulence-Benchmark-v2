def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    sum_missing = sum((x for x in range(a + 1, b) if x not in numbers[2:6]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]