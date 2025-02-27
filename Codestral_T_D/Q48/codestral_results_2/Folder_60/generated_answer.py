def return_binary_or_hexa(t):
    a, b = (t[38], t[52])
    s = sum(set(range(a + 1, b)) - set(t[38 + 1:52]))
    if s != 0:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    else:
        return ''