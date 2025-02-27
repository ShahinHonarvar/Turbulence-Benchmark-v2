def return_binary_or_hexa(t):
    a, b = (t[29], t[53])
    missing_sum = sum(set(range(a + 1, b)) - set(t[29:54]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:] if missing_sum else ''