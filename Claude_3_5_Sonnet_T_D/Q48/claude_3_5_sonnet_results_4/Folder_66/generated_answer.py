def return_binary_or_hexa(tuple_input):
    a = tuple_input[11]
    b = tuple_input[76]
    set_range = set(tuple_input[11:77])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in set_range))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]