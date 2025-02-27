def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[38]
    b = tuple_of_integers[81]
    total = sum((i for i in range(a + 1, b) if i not in tuple_of_integers[38:81]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]