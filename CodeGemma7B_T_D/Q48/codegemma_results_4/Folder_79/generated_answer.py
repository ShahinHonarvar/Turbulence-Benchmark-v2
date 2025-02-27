from functools import reduce

def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[1], int_tuple[7])
    lst = [i for i in range(a + 1, b) if i not in int_tuple[1:7]]
    total = reduce(lambda x, y: x + y, lst, 0)
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:].upper()