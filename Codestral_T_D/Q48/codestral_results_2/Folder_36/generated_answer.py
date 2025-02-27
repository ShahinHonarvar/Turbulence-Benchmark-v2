def return_binary_or_hexa(tupl):
    a = tupl[110]
    b = tupl[348]
    missing = set(range(a + 1, b)) - set(tupl[110:349])
    s = sum(missing)
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]