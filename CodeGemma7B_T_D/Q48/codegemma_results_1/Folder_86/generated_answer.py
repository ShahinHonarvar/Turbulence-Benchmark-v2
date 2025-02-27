def return_binary_or_hexa(tuple_of_ints):
    a, b = (tuple_of_ints[19], tuple_of_ints[32])
    filtered_list = [i for i in range(a + 1, b) if i not in tuple_of_ints[19:33]]
    if sum(filtered_list) % 2 == 1:
        return str(bin(sum(filtered_list))[2:])
    else:
        return hex(sum(filtered_list))[2:]