def return_binary_or_hexa(t):
    i = 110
    j = 348
    s = sum((k for k in range(t[i] + 1, t[j]) if k not in t[i:j]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()