def return_binary_or_hexa(tuple_input):
    a = tuple_input[1]
    b = tuple_input[7]
    sum_not_present = sum(set(range(a + 1, b)) - set(tuple_input[1:8]))
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()