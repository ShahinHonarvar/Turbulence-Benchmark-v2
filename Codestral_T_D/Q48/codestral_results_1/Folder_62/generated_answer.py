def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[92]
    s = sum((i for i in range(a + 1, b) if i not in tup[50:93]))
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:].lstrip('0') if s else ''