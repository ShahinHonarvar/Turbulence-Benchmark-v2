def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    s = set(range(a + 1, b))
    missing_sum = sum((i for i in s if i not in t[50:74]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]