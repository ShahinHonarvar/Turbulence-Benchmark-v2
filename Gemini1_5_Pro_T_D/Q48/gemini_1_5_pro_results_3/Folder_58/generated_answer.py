def return_binary_or_hexa(tuple_input):
    a = tuple_input[275]
    b = tuple_input[871]
    sum_result = 0
    for i in range(a + 1, b):
        if i not in tuple_input[275:871]:
            sum_result += i
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].upper()