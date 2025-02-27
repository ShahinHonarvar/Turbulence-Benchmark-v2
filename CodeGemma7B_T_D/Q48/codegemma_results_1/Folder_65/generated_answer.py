def return_binary_or_hexa(my_tuple):
    a = my_tuple[51]
    b = my_tuple[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple[51:77]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()