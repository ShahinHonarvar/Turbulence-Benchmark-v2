def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[11:12]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]