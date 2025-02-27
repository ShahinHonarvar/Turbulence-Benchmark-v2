def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[35:65]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]