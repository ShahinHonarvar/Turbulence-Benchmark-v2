def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[40]
    b = tuple_of_integers[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers[40:201]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
    return ''