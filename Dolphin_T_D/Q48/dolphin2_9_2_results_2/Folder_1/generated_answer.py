def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    missing = []
    for i in range(a + 1, b):
        if i not in t:
            missing.append(i)
    res_sum = sum(missing)
    if res_sum % 2 != 0:
        return bin(res_sum).replace('0b', '')
    else:
        return hex(res_sum).replace('0x', '')
    if len(missing) == 0:
        return ''