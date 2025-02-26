def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[97]
    set_between = set(tuple_input[10:98])
    sum_not_present = sum((x for x in range(a + 1, b) if x not in set_between))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]