def return_binary_or_hexa(lst):
    a = lst[10]
    b = lst[79]
    for i in range(a + 1, b):
        if i not in lst:
            if (i + a) % 2 != 0:
                return bin(i)[2:]
            else:
                return hex(i)[2:].upper()
    return ''