def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = 0
    miss = []
    for i in range(a + 1, b):
        if i not in t[35:70]:
            s += i
            miss.append(i)
    if not miss:
        return ''
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:]