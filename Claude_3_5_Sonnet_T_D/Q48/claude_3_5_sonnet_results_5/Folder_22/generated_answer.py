def return_binary_or_hexa(tuple_input):
    a = tuple_input[40]
    b = tuple_input[200]
    tuple_range = set(tuple_input[40:201])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]