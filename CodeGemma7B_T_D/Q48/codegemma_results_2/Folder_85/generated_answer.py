def return_binary_or_hexa(number_tuple):
    sum_of_missing_numbers = 0
    for i in range(number_tuple[1] + 1, number_tuple[8] - 1):
        if i not in number_tuple[1:8]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()