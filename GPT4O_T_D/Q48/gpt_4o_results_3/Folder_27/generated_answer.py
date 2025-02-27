def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    existing_numbers = set(numbers[87:89])
    sum_missing = sum((n for n in range(a + 1, b) if n not in existing_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]