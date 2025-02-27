def return_binary_or_hexa(t):
    a, b = (t[36], t[85])
    s = {x for x in t[36:86] if a < x < b}
    m = sum(set(range(a + 1, b)) - s)
    if not m:
        return ''
    return bin(m)[2:] if m % 2 else hex(m)[2:]