def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    total = sum([num for num in range(a + 1, b) if num not in tup[19:32]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].lower()