def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    missing_sum = 0
    for x in range(a + 1, b):
        if x not in t[13:71]:
            missing_sum += x
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]