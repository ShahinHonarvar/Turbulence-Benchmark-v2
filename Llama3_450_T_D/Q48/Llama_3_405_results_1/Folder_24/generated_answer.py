def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    present = set(t[14:91])
    total = set(range(a + 1, b))
    diff = total - present
    s = sum(diff)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]