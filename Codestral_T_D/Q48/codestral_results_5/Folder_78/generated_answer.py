def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[62]
    b = tuple_of_ints[96]
    s = sum((i for i in range(a + 1, b) if i not in tuple_of_ints[62:96]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]