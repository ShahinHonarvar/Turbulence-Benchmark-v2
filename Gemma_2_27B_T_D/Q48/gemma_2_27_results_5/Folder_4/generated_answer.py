def return_binary_or_hexa(my_tuple):
    a = my_tuple[49]
    b = my_tuple[74]
    total = 0
    for i in range(a + 1, b):
        if i not in my_tuple[49:74 + 1]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]