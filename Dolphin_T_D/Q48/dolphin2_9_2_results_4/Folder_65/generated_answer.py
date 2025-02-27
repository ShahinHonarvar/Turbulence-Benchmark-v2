def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    missing_sum = 0
    present = set(t[52:76])
    for i in range(a + 1, b):
        if i not in present:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()