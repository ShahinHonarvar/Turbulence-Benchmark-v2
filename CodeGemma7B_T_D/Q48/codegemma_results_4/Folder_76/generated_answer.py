def return_binary_or_hexa(int_tuple):
    max_index = max(int_tuple)
    sum_of_missing_num = sum(range(max_index + 1)) - sum(int_tuple)
    if sum_of_missing_num % 2 == 1:
        return str(bin(sum_of_missing_num))[2:]
    else:
        return hex(sum_of_missing_num)[2:].upper()