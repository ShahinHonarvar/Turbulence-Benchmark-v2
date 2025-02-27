def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[21:36]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]