def return_binary_or_hexa(numbers):
    a, b = (numbers[56], numbers[88])
    existing_numbers = set(numbers[57:88])
    sum_missing = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]