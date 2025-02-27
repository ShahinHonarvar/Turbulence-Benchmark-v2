def return_binary_or_hexa(tuple_of_numbers):
    a = tuple_of_numbers[51]
    b = tuple_of_numbers[76]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_of_numbers[51:77]:
            sum_of_numbers += i
    if sum_of_numbers % 2 != 0:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]