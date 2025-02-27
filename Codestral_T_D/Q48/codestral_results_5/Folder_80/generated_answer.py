def return_binary_or_hexa(tupl):
    a, b = (tupl[57], tupl[84])
    s = sum((i for i in range(a + 1, b) if i not in tupl[57:84]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]