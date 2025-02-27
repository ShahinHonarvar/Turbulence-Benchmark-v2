def return_binary_or_hexa(tuple_input):
    a = tuple_input[27]
    b = tuple_input[96]
    missing_numbers = [i for i in range(a + 1, b) if i not in tuple_input[27:96]]
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''