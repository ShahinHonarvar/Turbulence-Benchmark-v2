def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    sum = 0
    for i in range(a + 1, b):
        if i not in t[275:872]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    elif sum == 0:
        return ''
    else:
        return bin(sum)[2:]