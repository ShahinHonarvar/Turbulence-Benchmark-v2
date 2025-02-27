def return_binary_or_hexa(t):
    a, b = (t[10], t[76])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[10:77]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:] if missing_sum != 0 else ''