def return_binary_or_hexa(arg_tuple):
    if arg_tuple[34] + 1 >= arg_tuple[69] - 1:
        return ''
    non_present_elements = set(range(arg_tuple[34] + 1, arg_tuple[69] - 1)) - set(arg_tuple[35:68])
    sum_of_non_present_elements = sum(non_present_elements)
    if sum_of_non_present_elements % 2 == 0:
        return hex(sum_of_non_present_elements)
    else:
        return bin(sum_of_non_present_elements)[2:]