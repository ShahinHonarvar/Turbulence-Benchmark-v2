def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    num_set = set(numbers[70:97])
    sum_missing = sum((i for i in range(a + 1, b) if i not in num_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]