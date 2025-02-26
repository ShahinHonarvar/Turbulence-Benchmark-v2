def return_binary_or_hexa(tuple_input):
    a = tuple_input[55]
    b = tuple_input[84]
    tuple_range = set(tuple_input[55:85])
    sum_result = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].rstrip('L')