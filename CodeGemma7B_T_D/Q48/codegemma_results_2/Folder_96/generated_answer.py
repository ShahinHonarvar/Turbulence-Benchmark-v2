def return_binary_or_hexa(tup, a, b):
    """
    +50 +200
    """
    temp = ''
    for x in range(a + 1, b):
        if x not in tup:
            temp += str(x)
    if len(temp) == 0:
        return ''
    temp = int(temp)
    return bin(temp)[2:] if temp % 2 else hex(temp)[2:]