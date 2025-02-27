def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    R = range(a + 1, b)
    sum = 0
    present = [i for i in R if i in t]
    if all((i in t[10:13] for i in R)):
        return ''
    for x in R:
        if x not in present:
            sum += x
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]