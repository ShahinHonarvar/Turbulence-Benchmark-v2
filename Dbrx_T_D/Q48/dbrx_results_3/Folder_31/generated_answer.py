def return_binary_or_hexa(t):
    a, b = (t[33], t[78])
    missing_sum = sum((i for i in range(a + 1, b) if t[33:78] != list(range(t[33], t[78]))))
    if missing_sum % 2:
        return bin(missing_sum).split('0b')[1]
    else:
        return hex(missing_sum).split('0x')[1].upper()