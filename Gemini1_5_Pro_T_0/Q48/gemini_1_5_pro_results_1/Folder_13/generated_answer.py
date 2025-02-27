def return_binary_or_hexa(tup):
    a = tup[46]
    b = tup[91]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[46:92]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].lstrip('0')
    else:
        return bin(sum)[2:].lstrip('0')