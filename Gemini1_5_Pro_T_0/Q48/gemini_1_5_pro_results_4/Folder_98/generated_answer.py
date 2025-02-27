def return_binary_or_hexa(tup):
    a = tup[6]
    b = tup[7]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[6:8]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]