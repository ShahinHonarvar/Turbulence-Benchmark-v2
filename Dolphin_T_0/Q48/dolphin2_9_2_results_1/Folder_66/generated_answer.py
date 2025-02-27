def return_binary_or_hexa(t):
    a, b = (t[11], t[76])
    s = set(range(a + 1, b))
    s.difference_update(t[11:77])
    if a + 1 <= sum(s) <= b - 1 and sum(s) % 2 != 0:
        return bin(sum(s))[2:]
    elif a + 1 <= sum(s) <= b - 1 and sum(s) % 2 == 0:
        return hex(sum(s))[2:]
    else:
        return ''