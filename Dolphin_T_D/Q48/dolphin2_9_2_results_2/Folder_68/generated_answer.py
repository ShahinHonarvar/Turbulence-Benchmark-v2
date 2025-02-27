def return_binary_or_hexa(t):
    a = t[0]
    b = t[9]
    missing_sum = 0
    inclusives = set(range(a + 1, b))
    for i in range(len(t)):
        if t[i] in inclusives:
            inclusives.remove(t[i])
    missing_sum = sum(inclusives)
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]