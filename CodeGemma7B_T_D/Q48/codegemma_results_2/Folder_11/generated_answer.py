def return_binary_or_hexa(T):
    a, b = (T[48], T[76])
    res = sum(set(range(a + 1, b)) - set(T[48:77]))
    return bin(res)[2:] if res % 2 else hex(res)[2:].upper()