def return_binary_or_hexa(t):
    a = t[35]
    b = t[64] if len(t) > 64 else t[-1]
    x = sum(set(range(a + 1, b)) - set(t[36:64]))
    return bin(x)[2:] if x % 2 else hex(x)[2:].upper() if x else ''