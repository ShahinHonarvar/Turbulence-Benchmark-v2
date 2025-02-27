def return_binary_or_hexa(u):
    a, b = (u[43], u[70])
    s = 0
    for i in range(a + 1, b):
        if i not in u[43:71]:
            s += i
    r = bin(s)[2:] if s & 1 else hex(s)[2:].lower()
    return r if s else ''