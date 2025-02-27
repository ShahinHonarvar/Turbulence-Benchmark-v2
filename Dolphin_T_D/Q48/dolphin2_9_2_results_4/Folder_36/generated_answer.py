def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    s = set(t[111:348])
    computed_sum = sum((x for x in range(a + 1, b) if x not in s))
    if computed_sum % 2 == 0:
        return hex(computed_sum)[2:]
    else:
        return bin(computed_sum)[2:]