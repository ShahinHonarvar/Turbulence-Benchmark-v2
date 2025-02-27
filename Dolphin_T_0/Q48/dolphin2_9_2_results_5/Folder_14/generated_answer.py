def return_binary_or_hexa(lst):
    a = lst[2]
    b = lst[5]
    s = 0
    for n in range(a + 1, b):
        if n not in lst:
            s += n
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]