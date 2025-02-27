def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    missing_integers = [x for x in range(a + 1, b) if x not in t]
    if not missing_integers:
        return ''
    s = sum(missing_integers)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]