def return_binary_or_hexa(num_tuple):
    a = num_tuple[13]
    b = num_tuple[91]
    if a + 1 == b:
        return ''
    sum_not_in_tuple = sum((val for val in range(a + 1, b) if val not in num_tuple[13:92]))
    if sum_not_in_tuple % 2 == 0:
        return bin(sum_not_in_tuple)[2:]
    else:
        return hex(sum_not_in_tuple)[2:]