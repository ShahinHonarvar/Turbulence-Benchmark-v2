def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    if a + 1 > b:
        return ''
    sum = 0
    for i in range(a + 1, b + 1):
        if not i in t[17:88 + 1]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)