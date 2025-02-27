def return_binary_or_hexa(tup):
    a, b = (tup[40], tup[200])
    missing = [i for i in range(a + 1, b) if i not in tup[40:201]]
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]