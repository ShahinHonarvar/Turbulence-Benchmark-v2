def return_binary_or_hexa(tuple_input):
    a = tuple_input[0]
    b = tuple_input[8]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_input:
            sum_of_numbers += i
    if sum_of_numbers == 0:
        return ''
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]