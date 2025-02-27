def return_binary_or_hexa(t):
    s = sum((f for f in range(t[20] + 1, t[36]) if f not in t[20:37]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()