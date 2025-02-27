def return_binary_or_hexa(x):
    a = x[38]
    b = x[81]
    s = sum((i for i in range(a + 1, b) if i not in x[38:82]))
    return bin(s)[2:] if s & 1 else hex(s)[2:].lower()