def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    used = [False] * 100
    for i in t:
        used[i] = True
    sum = 0
    for i in range(a + 1, b):
        if not used[i]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    return bin(sum)[2:]