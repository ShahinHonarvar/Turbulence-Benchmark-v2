def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[1:6]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]