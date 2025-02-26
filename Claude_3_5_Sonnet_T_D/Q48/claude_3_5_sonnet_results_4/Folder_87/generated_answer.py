def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[43]
    excluded_numbers = set(tuple_input[20:44])
    sum_of_numbers = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_of_numbers == 0:
        return ''
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()