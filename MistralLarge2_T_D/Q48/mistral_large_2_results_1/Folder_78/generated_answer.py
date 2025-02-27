def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    subset = set(numbers[62:97])
    sum_missing = sum((x for x in range(a + 1, b) if x not in subset))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()