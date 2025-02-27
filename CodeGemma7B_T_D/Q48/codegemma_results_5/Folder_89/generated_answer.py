def return_binary_or_hexa(my_tuple):
    a = my_tuple[55]
    b = my_tuple[84]
    num = 0
    my_set = set(my_tuple[55:85])
    for i in range(a + 1, b):
        if i not in my_set:
            num += i
    if num % 2:
        return bin(num)[2:]
    else:
        return hex(num)[2:].upper()