def return_binary_or_hexa(t):
    a = t[50]
    b = t[92]
    s = sum(range(a + 1, b)) - sum(t[51:92])
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]