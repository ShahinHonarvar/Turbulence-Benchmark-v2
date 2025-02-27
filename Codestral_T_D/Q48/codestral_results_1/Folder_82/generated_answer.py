def return_binary_or_hexa(t):
    a, b = (t[20], t[200])
    missing = set(range(a + 1, b)) - set(t[20:200])
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:]