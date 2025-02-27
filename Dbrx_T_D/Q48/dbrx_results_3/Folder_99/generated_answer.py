def return_binary_or_hexa(int_tuple):
    a = int_tuple[426]
    b = int_tuple[668]
    sum_of_numbers = sum(set(range(a + 1, b)) - set(int_tuple[427:669]))
    if sum_of_numbers % 2 != 0:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:].upper()