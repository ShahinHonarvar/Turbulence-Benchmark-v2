def return_binary_or_hexa(tuple_input):
    a = tuple_input[7]
    b = tuple_input[9]
    sum_not_present = sum((num for num in range(a + 1, b) if num not in tuple_input[7:10]))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 != 0:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]