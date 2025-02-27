def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    s = 0
    counter = 0
    for i in range(a + 1, b):
        if i in t[56:89]:
            counter += 1
            continue
        s += i
    if counter == b - a - 1:
        return ''
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]