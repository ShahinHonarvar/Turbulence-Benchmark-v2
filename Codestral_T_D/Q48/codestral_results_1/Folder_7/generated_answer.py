def return_binary_or_hexa(tupl):
    a = tupl[10]
    b = tupl[97]
    s = sum((i for i in range(a + 1, b) if i not in tupl[10:97]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''