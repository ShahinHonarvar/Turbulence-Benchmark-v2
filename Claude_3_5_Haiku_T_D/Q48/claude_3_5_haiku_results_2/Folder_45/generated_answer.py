def return_binary_or_hexa(tuple_input):
    a = tuple_input[30]
    b = tuple_input[200]
    missing_numbers = []
    for num in range(a + 1, b):
        if num not in tuple_input[30:201]:
            missing_numbers.append(num)
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]