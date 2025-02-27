def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    a += 1
    xor = 0
    for i in range(a, b):
        if i not in t[69:98]:
            xor ^= i
    return bin(xor)[2:] if xor % 2 else hex(xor)[2:].lower() if xor % 2 else ''