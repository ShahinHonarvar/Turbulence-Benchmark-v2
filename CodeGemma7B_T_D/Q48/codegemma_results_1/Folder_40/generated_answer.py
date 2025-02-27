def return_binary_or_hexa(t):
    l, r = (t[0] + 1, t[3])
    if all((i in range(l, r + 1) for i in t[4:])):
        return ''
    sumx = sum(range(l, r + 1)) - sum(t[4:])
    if sumx % 2 == 1:
        return bin(sumx)[2:]
    else:
        return hex(sumx)[2:]