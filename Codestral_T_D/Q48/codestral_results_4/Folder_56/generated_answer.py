def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[7:10]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]