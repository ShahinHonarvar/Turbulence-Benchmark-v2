def return_binary_or_hexa(tuple_of_ints):
    a, b = (tuple_of_ints[73], tuple_of_ints[84])
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_ints[73:85]:
            sum += i
    return bin(sum)[2:] if sum % 2 == 1 else hex(sum)[2:].upper()