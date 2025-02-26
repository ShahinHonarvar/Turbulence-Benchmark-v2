def return_binary_or_hexa(tuple_input):
    a = tuple_input[275]
    b = tuple_input[871]
    tuple_range = set(tuple_input[275:872])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 != 0:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]