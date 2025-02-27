def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[13]
    b = tuple_of_ints[35]
    total_sum = sum((i for i in range(a + 1, b) if i not in tuple_of_ints[13:36]))
    if not total_sum:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]