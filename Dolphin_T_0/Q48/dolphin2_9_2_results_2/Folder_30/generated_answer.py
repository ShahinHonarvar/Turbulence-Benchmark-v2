def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    missing = [x for x in range(a + 1, b) if x not in t[22:25]]
    if len(missing) == 0:
        return ''
    t_sum = sum(missing)
    if t_sum % 2 == 1:
        return bin(t_sum)[2:]
    else:
        return hex(t_sum)[2:]