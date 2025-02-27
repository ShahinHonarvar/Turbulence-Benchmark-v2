def return_binary_or_hexa(lst):
    a = lst[51]
    b = lst[76]
    s = sum((n for n in range(a + 1, b) if n not in lst[51:77]))
    if s % 2 == 0:
        return str(hex(s))[2:]
    else:
        return str(bin(s))[2:]