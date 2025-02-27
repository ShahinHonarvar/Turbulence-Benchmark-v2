def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    if sorted(range(a + 1, b)) == sorted(t[43:87]):
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in t[43:87]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]