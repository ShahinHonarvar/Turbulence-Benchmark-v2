def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    result = sum(set(range(a + 1, b)) - set(t[3:8]))
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]