def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[5]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[2:5]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]