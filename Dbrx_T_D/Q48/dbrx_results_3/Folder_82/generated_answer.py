def return_binary_or_hexa(tup):
    a, b = (tup[20], tup[200])
    if a + 1 > b - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[20:201]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()