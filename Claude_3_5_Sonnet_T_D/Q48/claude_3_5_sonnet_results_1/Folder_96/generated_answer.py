def return_binary_or_hexa(tuple_input):
    a = tuple_input[50]
    b = tuple_input[200]
    set_between = set(tuple_input[50:201])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in set_between))
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].rstrip('L')