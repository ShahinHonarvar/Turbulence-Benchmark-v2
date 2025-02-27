def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    present_numbers = set(numbers[69:99])
    sum_missing = sum((x for x in range(a + 1, b) if x not in present_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]