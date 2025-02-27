def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[36]
    b = tuple_of_integers[52]
    numbers_in_range = [num for num in range(a + 1, b) if num not in tuple_of_integers]
    if numbers_in_range:
        sum_of_numbers = sum(numbers_in_range)
        if sum_of_numbers % 2:
            return bin(sum_of_numbers)[2:]
        else:
            return hex(sum_of_numbers)[2:]
    return ''