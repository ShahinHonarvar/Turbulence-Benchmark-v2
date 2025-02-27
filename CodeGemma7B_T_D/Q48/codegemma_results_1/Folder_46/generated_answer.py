def return_binary_or_hexa(tup):
    a, b = (tup[10], tup[79])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[10:79]:
            sum += i
    if sum % 2:
        return str(bin(sum))[2:]
    else:
        return str(hex(sum))[2:].lower()