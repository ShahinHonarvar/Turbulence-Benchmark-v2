def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    present = set(t[1:6])
    not_present = [i for i in range(a + 1, b) if i not in present]
    s = sum(not_present)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s).upper()[2:]
    else:
        return bin(s)[2:]