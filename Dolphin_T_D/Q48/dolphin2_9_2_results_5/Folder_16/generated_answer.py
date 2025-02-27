def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    s = sum(range(a + 1, b))
    for i in t[90:98]:
        if i in range(a + 1, b):
            s -= i
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 == 1 else hex(s)[2:]