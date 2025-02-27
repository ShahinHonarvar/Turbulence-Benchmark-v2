def return_binary_or_hexa(tuple_int):
    a = tuple_int[37]
    b = tuple_int[43]
    sum_lost = sum((i for i in range(a + 1, b) if i not in tuple_int[37:44]))
    result = '0x{:0>x}' if sum_lost % 2 else '{:b}'
    return result.format(sum_lost)