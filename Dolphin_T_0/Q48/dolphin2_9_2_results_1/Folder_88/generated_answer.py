def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    to_sum = [x for x in range(a + 1, b) if x not in t[3:10]]
    if len(to_sum) == 0:
        return ''
    summ = sum(to_sum)
    if summ % 2 == 0:
        return hex(summ)[2:]
    else:
        return bin(summ)[2:]