def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[0]
    b = tuple_of_integers[2]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]