def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    if sum != 0:
        return bin(sum)[2:] if sum % 2 != 0 else hex(sum)[2:]
    else:
        return ''