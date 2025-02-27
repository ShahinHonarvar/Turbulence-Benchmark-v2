def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    subset = set(numbers[10:77])
    sum_missing = sum((i for i in range(a + 1, b) if i not in subset))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()