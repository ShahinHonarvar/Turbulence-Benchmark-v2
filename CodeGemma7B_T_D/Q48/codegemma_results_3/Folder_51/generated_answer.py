def return_binary_or_hexa(t):
    res = 0
    for num in range(t[6] + 1, t[9]):
        if num not in t[6:9]:
            res += num
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()