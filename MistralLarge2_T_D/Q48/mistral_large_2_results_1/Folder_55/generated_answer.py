def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    sum_missing = sum((i for i in range(a + 1, b) if i not in numbers[10:13]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]