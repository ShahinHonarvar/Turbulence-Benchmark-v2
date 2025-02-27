def return_binary_or_hexa(tuple_input):
    a = tuple_input[1]
    b = tuple_input[8]
    sum_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_input[1:9]:
            sum_numbers += i
    if sum_numbers == 0:
        return ''
    if sum_numbers % 2 == 1:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:]