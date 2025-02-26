def return_binary_or_hexa(tuple_input):
    a = tuple_input[427]
    b = tuple_input[669]
    set_between = set(tuple_input[427:670])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in set_between))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 != 0:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]