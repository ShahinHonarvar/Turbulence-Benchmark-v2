def return_binary_or_hexa(t):
    s = sum(range(t[44] + 1, t[91]))
    if s % 2:
        return str(bin(s))[2:]
    return str(hex(s))[2:].upper()