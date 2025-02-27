def return_binary_or_hexa(t):
    a = t[20]
    b = t[93]
    missing = [x for x in range(a + 1, b) if x not in t]
    s = sum(missing)
    return bin(s).replace('0b', '') if s % 2 == 1 else hex(s).replace('0x', '')