def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    between_a_b = [x for x in range(a + 1, b) if x not in t[43:87]]
    if not between_a_b:
        return ''
    s = sum(between_a_b)
    if s & 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]