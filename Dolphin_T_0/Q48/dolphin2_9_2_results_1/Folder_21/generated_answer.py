def return_binary_or_hexa(t):
    a, b = (t[15] + 1, t[-57] - 1)
    missing = [i for i in range(a, b + 1) if i not in t]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]