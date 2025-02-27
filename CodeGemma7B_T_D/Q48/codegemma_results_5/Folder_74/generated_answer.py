def return_binary_or_hexa(t):
    j, a, b = (0, t[69], t[97])
    s = 0
    while j <= b - a - 1:
        s += j + a + 1
        j += 1
    if s % 2 == 0:
        return f'{s:x}'
    else:
        return f'{s:b}'