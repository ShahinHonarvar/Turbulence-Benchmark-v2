def return_binary_or_hexa(ls):
    a, b = (ls[46], ls[91])
    missing = [i for i in range(a + 1, b) if i not in ls[47:91]]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]