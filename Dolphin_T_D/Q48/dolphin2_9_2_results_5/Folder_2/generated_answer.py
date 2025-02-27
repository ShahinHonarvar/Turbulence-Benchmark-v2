def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    missing = []
    for i in range(a + 1, b):
        if i not in t[73:93]:
            missing.append(i)
    _sum = sum(missing)
    if _sum % 2 == 0:
        return hex(_sum)[2:]
    else:
        return bin(_sum)[2:]