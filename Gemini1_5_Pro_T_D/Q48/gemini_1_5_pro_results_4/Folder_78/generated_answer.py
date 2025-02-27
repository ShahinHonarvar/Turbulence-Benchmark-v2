def return_binary_or_hexa(tuple_input):
    a = tuple_input[62]
    b = tuple_input[96]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_input[62:97]:
            sum_of_numbers += i
    if sum_of_numbers == 0:
        return ''
    elif sum_of_numbers % 2 == 0:
        return hex(sum_of_numbers)[2:].upper()
    else:
        return bin(sum_of_numbers)[2:]