def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    s = set(range(a + 1, b))
    t = set(t[20:36])
    s = s - t
    sum_s = sum(s)
    if sum_s % 2 == 1:
        return bin(sum_s)[2:]
    else:
        return hex(sum_s)[2:]