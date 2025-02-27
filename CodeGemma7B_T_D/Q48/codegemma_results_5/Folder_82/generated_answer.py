def return_binary_or_hexa(t):
    s = sum(set(range(t[20] + 1, t[200] + 1)).difference(t[20:200]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()