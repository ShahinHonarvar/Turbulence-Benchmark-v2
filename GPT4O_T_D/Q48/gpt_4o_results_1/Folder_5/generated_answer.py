def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    sum_missing = sum((x for x in range(a + 1, b) if x not in numbers[2:9]))
    if not sum_missing:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:]