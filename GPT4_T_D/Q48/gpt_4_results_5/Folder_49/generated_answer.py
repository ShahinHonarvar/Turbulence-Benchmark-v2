def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    complete_set = set(range(a + 1, b))
    subset = set(numbers[80:201])
    missing_set = complete_set - subset
    sum_missing = sum(missing_set)
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()