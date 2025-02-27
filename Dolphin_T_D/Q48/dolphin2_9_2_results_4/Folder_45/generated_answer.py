def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    missing = [i for i in range(a + 1, b) if i not in t[30:201]]
    if not missing:
        return ''
    sum = 0
    for i in missing:
        sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]