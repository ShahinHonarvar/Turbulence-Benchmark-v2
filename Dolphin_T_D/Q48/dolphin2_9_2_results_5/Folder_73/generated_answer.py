def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[10]
    b = tuple_of_integers[76]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers:
            sum_ += i
    if sum_ % 2 == 0:
        return hex(sum_)[2:].upper()
    else:
        return bin(sum_)[2:]
    return ''