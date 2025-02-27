def return_binary_or_hexa(tuple_of_int):
    a = tuple_of_int[7]
    b = tuple_of_int[9]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_int[7:10]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()