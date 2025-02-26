def return_binary_or_hexa(tuple_input):
    a = tuple_input[44]
    b = tuple_input[91]
    missing_numbers = set(range(a + 1, b))
    for num in tuple_input[44:92]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]