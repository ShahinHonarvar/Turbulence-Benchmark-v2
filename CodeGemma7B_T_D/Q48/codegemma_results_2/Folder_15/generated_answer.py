def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    sum = 0
    for num in range(a + 1, b):
        if not num in t[0:5]:
            sum += num
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]