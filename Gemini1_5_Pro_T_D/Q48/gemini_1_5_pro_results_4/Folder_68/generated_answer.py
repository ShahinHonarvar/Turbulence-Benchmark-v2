def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[0]
    b = tuple_of_integers[9]
    summation = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers:
            summation += i
    if summation == 0:
        return ''
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]