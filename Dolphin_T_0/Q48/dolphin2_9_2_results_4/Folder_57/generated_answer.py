def return_binary_or_hexa(t):
    a = t[25] + 1
    b = t[80] - 1
    s = sum(range(a, b + 1)) - sum(t[25:81])
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]