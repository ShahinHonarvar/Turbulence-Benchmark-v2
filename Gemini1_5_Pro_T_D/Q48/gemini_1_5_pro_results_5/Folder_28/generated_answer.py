def return_binary_or_hexa(tuple_input):
    a = tuple_input[86]
    b = tuple_input[99]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_input[86:100]:
            sum_of_numbers += i
    if sum_of_numbers == 0:
        return ''
    elif sum_of_numbers % 2 == 0:
        return hex(sum_of_numbers)[2:].lstrip('0')
    else:
        return bin(sum_of_numbers)[2:].lstrip('0')