def return_binary_or_hexa(my_tuple):
    a = my_tuple[27]
    b = my_tuple[96]
    value = 0
    for item in range(a + 1, b):
        if item not in my_tuple[27:97]:
            value += item
    if value % 2 == 0:
        return hex(value)[2:].upper()
    else:
        return bin(value)[2:]