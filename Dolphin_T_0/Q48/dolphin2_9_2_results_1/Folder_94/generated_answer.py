def return_binary_or_hexa(t):
    a = t[42]
    b = t[87]
    s = [i for i in range(a + 1, b) if i not in t[43:87]]
    if not s:
        return ''
    sum_s = sum(s)
    if sum_s % 2:
        return bin(sum_s)[2:]
    else:
        return hex(sum_s)[2:].upper()