def return_binary_or_hexa(t):
    a, b = (t[43], t[70])
    s = sum((x for x in range(a + 1, b) if x not in t[43 + 1:70]))
    if s > 0:
        return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]
    else:
        return ''