def return_binary_or_hexa(num_tuple):
    initial_index = 45
    final_index = 48
    sum_of_missing_numbers = 0
    element_counter = initial_index
    while element_counter <= final_index:
        if num_tuple[element_counter] != element_counter:
            sum_of_missing_numbers += element_counter
        element_counter += 1
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:].upper()
    else:
        return bin(sum_of_missing_numbers)[2:]