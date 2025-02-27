def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    sum_non_presence = sum((i for i in range(a + 1, b) if i not in tup[25:81]))
    if sum_non_presence % 2:
        return bin(sum_non_presence)[2:]
    else:
        return hex(sum_non_presence)[2:].upper()