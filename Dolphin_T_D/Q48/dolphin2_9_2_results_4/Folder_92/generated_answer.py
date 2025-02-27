def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    a_b = set(range(a + 1, b))
    if a_b.issubset(map(int, t)):
        return ''
    else:
        sum = a_b - set(t[1])
        if sum % 2 == 0:
            return hex(sum)
        else:
            return bin(sum)