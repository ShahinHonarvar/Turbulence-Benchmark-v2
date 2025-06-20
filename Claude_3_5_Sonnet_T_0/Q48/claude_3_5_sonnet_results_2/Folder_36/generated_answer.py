def return_binary_or_hexa(tuple_input):
    a = tuple_input[110]
    b = tuple_input[348]
    set_between = set(tuple_input[110:349])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in set_between))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]