def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[8]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[1:8]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    elif sum > 0:
        return hex(sum)[2:]
    else:
        return ''