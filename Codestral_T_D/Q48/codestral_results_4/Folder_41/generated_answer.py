def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[3:8]))
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]