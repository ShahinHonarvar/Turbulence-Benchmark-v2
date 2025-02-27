def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[:3]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    elif sum == 0:
        return ''
    else:
        return hex(sum)[2:]