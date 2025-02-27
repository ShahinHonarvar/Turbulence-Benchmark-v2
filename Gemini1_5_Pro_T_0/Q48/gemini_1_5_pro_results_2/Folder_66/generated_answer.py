def return_binary_or_hexa(tuple_input):
    a = tuple_input[11]
    b = tuple_input[76]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_input[11:77]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]