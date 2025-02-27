def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    if all((i + 1 in t[1:10] for i in range(a, b - 1))):
        return ''
    else:
        sum = 0
        for i in range(a + 1, b):
            if i not in t[1:10]:
                sum += i
        if sum % 2 == 1:
            return bin(sum)[2:]
        else:
            return hex(sum)[2:]