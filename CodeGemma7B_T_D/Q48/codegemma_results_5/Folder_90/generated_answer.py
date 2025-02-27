def return_binary_or_hexa(t):
    a, b = (t[60], t[90])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t[60:91]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]