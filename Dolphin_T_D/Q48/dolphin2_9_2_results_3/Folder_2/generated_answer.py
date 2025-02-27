def return_binary_or_hexa(t):
    a, b = (t[72], t[93])
    missing = [i for i in range(a + 1, b) if i not in t[73:93]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()