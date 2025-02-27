def return_binary_or_hexa(t):
    if t[0] + 1 > t[4] - 1:
        return ''
    sum = 0
    present = set(t[0:5])
    for i in range(t[0] + 1, t[4]):
        if i not in present:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:]