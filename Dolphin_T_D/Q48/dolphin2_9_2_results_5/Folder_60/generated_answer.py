def return_binary_or_hexa(t):
    a, b = (t[38], t[52])
    if all((x in t for x in range(a + 1, b))):
        return ''
    res = sum(set(range(a + 1, b + 1)) - set(t[39:52]))
    return bin(res)[2:] if res % 2 else hex(res)[2:]