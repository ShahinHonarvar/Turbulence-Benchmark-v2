def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    missing_sum = 0
    for i in range(a + 1, b):
        if not i in t:
            missing_sum += i
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
    return ''