def return_binary_or_hexa(input_tuple):
    a = input_tuple[44]
    b = input_tuple[78]
    sum_unpresented = 0
    for i in range(a + 1, b):
        if i in input_tuple[44:79]:
            sum_unpresented += i
    sum_unpresented_str = str(sum_unpresented)
    if sum_unpresented % 2 == 0:
        return_str = hex(sum_unpresented)[2:]
    else:
        return_str = bin(sum_unpresented)[2:]
    return return_str