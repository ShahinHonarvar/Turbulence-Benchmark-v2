def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[20]
    b = integer_tuple[93]
    sum_of_missing_numbers = 0
    for number in range(a + 1, b):
        if number not in integer_tuple[20:94]:
            sum_of_missing_numbers += number
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()