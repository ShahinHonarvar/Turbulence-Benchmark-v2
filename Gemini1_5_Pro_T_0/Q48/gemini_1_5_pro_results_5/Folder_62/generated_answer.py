def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[50]
    b = tuple_of_integers[92]
    sum_of_missing_integers = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers[51:92]:
            sum_of_missing_integers += i
    if sum_of_missing_integers == 0:
        return ''
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]