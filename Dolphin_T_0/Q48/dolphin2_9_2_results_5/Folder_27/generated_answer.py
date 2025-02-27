def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    s = [i for i in range(a + 1, b) if i not in t[86:89]]
    if all((i in t[86:90] for i in range(a + 1, b))):
        return ''
    else:
        sum = 0
        for i in s:
            sum += i
        if sum % 2 == 0:
            return hex(sum)[2:]
        else:
            return bin(sum)[2:]