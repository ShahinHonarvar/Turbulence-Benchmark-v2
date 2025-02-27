def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    n = [x for x in range(a + 1, b)]
    diff = [i for i in n if i not in t]
    s = sum(diff)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]