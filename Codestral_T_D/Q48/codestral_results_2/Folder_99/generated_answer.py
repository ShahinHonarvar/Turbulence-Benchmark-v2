def return_binary_or_hexa(t):
    a, b = (t[427], t[669])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[427:669]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]