def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t:
            missing_sum += i
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]