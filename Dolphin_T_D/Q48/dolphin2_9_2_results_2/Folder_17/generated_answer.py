def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    p = [x for x in t if 74 <= t.index(x) <= 83 and (x < a or x > b)]
    if not p:
        return ''
    s = sum(range(a + 1, b)) - sum(p)
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]