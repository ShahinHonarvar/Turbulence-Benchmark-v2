def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    if a >= b:
        return ''
    m1 = max(1, a)
    m2 = min(1000, b)
    m3 = set(range(m1, m2 + 1))
    m4 = set(t[60:90])
    m5 = m3 - m4
    m6 = sum(m5)
    if m6 % 2 == 0:
        return hex(m6)[2:]
    else:
        return bin(m6)[2:]