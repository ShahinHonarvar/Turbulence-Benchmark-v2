def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    missing_sum = sum(set(range(a + 1, b)) - set(t[56:91]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper() if missing_sum else ''