def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[28]
    sum_not_present = sum(set(range(a + 1, b)) - set(tuple_input[10:29]))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()