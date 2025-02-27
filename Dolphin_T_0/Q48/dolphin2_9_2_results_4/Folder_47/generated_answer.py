def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    numbers = set(t)
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
    if not sum:
        return ''
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]