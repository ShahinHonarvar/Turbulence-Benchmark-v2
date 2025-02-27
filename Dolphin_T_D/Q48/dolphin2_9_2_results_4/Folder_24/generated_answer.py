def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    values = set(range(a + 1, b))
    missing = values.difference(numbers[14:92])
    if not missing:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()