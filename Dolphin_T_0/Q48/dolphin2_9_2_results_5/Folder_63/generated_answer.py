def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    sum = [i for i in range(a + 1, b) if i not in tup[81:86]]
    if sum:
        if sum[-1] % 2 == 1:
            return str(bin(sum[-1]))[2:]
        else:
            return hex(sum[-1])[2:]
    else:
        return ''