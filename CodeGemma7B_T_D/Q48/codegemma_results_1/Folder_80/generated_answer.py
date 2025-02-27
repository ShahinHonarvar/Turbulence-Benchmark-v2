def return_binary_or_hexa(tup):
    output = []
    a, b = tup
    for i in range(a + 1, b + 1):
        if i not in tup[57:85]:
            output.append(i)
    s = sum(output)
    if s % 2:
        return str(bin(s))[2:]
    else:
        return str(hex(s))[2:].upper()