def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[8])
    m = b - a
    k = [i for i in range(a + 1, b) if i not in tup[2:9]]
    return bin(sum(k))[2:] if sum(k) % 2 else hex(sum(k))[2:].upper() if m else ''