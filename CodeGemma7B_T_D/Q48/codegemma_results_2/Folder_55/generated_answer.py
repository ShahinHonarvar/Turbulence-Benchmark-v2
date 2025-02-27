def return_binary_or_hexa(t):
    i, j, l = (10, 12, sum(t[i + 1:j + 1]))
    v = [ii for ii in range(t[i] + 1, t[j] + 1) if ii not in t[i + 1:j + 1]]
    for x in v:
        l += x
    return bin(l)[2:].zfill(4) if l % 2 else hex(l)[2:].zfill(4)