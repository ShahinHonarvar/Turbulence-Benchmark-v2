def return_binary_or_hexa(t):
    a, b = (t[50], t[200])
    M = set(t[50:201])
    S = 0
    R = 0
    for n in range(a + 1, b):
        S += n
        if n not in M:
            R += n
    if S & 1 == 0:
        return hex(R)[2:].upper()
    else:
        return bin(R)[2:]