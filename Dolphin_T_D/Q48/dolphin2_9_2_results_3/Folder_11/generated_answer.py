def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[48]
    b = tuple_of_integers[76]
    missing_numbers = [n for n in range(a + 1, b) if n not in tuple_of_integers]
    sum_of_missing_numbers = sum(missing_numbers)
    if len(missing_numbers) == 0:
        return ''
    elif sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()