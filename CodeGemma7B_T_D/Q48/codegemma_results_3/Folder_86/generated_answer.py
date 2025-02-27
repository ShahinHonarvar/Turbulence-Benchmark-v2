def return_binary_or_hexa(tup):
    a, b = (tup[19], tup[32])
    xor = 0
    for n in range(a + 1, b):
        if n not in tup[19:33]:
            xor ^= n
    return bin(xor)[2:] if xor % 2 else hex(xor)[2:].upper()