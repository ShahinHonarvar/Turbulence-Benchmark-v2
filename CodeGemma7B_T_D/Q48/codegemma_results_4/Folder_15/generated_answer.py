def return_binary_or_hexa(number_tuple):
    first_num = number_tuple[0]
    last_num = number_tuple[4]
    sum_of_missing_numbers = 0
    for number in range(first_num + 1, last_num):
        if number not in number_tuple:
            sum_of_missing_numbers += number
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()