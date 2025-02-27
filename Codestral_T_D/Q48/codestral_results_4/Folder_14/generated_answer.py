def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[2:5]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]