def return_binary_or_hexa(t):
    a, b = (t[10], t[97])
    missing_sum = sum(set(range(a + 1, b)) - set(t[10:97]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()