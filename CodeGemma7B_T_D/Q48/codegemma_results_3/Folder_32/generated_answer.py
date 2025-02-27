def return_binary_or_hexa(tuple_ints):
    sum_missing_numbers = 0
    for i in range(tuple_ints[86] + 1, tuple_ints[90]):
        if i not in tuple_ints[86:91]:
            sum_missing_numbers += i
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()