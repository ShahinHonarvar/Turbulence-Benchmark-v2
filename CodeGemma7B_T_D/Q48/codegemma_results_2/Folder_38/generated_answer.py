def return_binary_or_hexa(t):
    s = sum([i for i in range(t[36] + 1, t[85] + 1) if i not in t[36:85]])
    return str(bin(s))[2:] if s % 2 else hex(s)[2:].upper()