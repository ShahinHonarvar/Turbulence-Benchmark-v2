def return_binary_or_hexa(t):
    a = t[77]
    b = t[84]
    s = set(range(a + 1, b))
    p = set(t[78:84])
    n = sum(s - p)
    if n == 0:
        return ''
    elif n % 2 == 1:
        return bin(n)[2:]
    else:
        return hex(n)[2:]