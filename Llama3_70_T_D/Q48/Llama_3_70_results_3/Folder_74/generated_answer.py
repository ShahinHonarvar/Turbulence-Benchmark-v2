def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    total = sum((i for i in range(a + 1, b) if i not in t[69:98]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]