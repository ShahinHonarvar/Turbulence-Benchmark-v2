def return_binary_or_hexa(tuple_input):
    a = tuple_input[18]
    b = tuple_input[52]
    excluded_numbers = set(tuple_input[18:53])
    sum_of_numbers = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_of_numbers == 0:
        return ''
    elif sum_of_numbers % 2 != 0:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].rstrip('L')