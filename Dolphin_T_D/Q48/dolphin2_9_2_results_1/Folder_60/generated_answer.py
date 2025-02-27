def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    total = sum(t[39:52])
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]