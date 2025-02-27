def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    existing_numbers = set(numbers[1:5])
    sum_missing = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]