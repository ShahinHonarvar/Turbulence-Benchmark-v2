def return_binary_or_hexa(tup):
    a, b = (tup[39], tup[43])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[39:44]:
            sum += i
    return bin(sum)[2:].zfill(len(bin(b - a)[2:])) if sum % 2 else hex(sum)[2:].zfill(len(hex(b - a)[2:]))