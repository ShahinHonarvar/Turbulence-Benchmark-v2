def return_binary_or_hexa(tuple_of_ints):
    a, b = (tuple_of_ints[56], tuple_of_ints[84])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_ints[57:86]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()