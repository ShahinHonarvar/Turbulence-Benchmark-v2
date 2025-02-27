def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[50], int_tuple[200])
    sum_of_missing_numbers = sum(set(range(a + 1, b)) - set(int_tuple[51:199]))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)