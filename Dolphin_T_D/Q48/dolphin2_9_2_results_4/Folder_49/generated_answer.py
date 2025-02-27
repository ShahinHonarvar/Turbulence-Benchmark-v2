def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    all_numbers = set(range(a + 1, b))
    subset = set(numbers[81:201])
    missing = all_numbers - subset
    if not missing:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]