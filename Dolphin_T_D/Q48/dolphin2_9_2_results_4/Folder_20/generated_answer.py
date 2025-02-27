def return_binary_or_hexa(my_tuple):
    a, b = (my_tuple[27], my_tuple[96])
    missing = [i for i in range(a + 1, b) if i not in my_tuple[27:97]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]