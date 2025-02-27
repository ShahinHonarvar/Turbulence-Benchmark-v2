def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[0]
    b = tuple_of_ints[5]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_ints:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()