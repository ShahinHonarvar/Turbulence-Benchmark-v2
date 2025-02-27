def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    missing_sum = sum(set(range(a + 1, b)) - set(t[43:87]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]