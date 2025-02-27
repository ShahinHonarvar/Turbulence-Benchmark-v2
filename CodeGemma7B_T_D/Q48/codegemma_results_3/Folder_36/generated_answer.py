import math

def return_binary_or_hexa(tuple):
    a = tuple[110] + 1
    b = tuple[348] - 1
    int_list = list(range(a, b + 1))
    for i in range(110, 349):
        if tuple[i] in int_list:
            int_list.remove(tuple[i])
    sum = sum(int_list)
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]