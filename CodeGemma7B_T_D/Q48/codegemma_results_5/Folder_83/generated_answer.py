def return_binary_or_hexa(dist_int_tuple):
    a = dist_int_tuple[90]
    b = dist_int_tuple[200]
    my_sum = 0
    for i in range(a + 1, b):
        if i not in dist_int_tuple[90:201]:
            my_sum += i
    if my_sum % 2 == 1:
        return bin(my_sum)[2:]
    else:
        return hex(my_sum)[2:].upper()