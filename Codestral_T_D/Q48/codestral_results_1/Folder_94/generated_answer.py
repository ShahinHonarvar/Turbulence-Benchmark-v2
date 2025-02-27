def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    missing = [i for i in range(a + 1, b) if i not in t[42:88]]
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]