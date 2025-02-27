def return_binary_or_hexa(tup):
    b, a = (tup[43], tup[39])
    sm = 0
    for i in range(a + 1, b):
        if i not in tup[39:44]:
            sm += i
    if sm % 2:
        return str(bin(sm))[2:]
    else:
        return hex(sm)[2:].upper() if sm > 15 else hex(sm)[2:]