def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    missing = [x for x in range(a + 1, b) if x not in t]
    a_sum = sum(missing)
    if a_sum % 2 == 0:
        return hex(a_sum)[2:]
    else:
        return bin(a_sum)[2:]