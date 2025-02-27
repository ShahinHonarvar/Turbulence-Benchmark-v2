def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t[42:88]:
            missing_sum += i
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()