def return_binary_or_hexa(t):
    sum = 0
    for i in range(t[1] + 1, t[8]):
        if i not in t:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]