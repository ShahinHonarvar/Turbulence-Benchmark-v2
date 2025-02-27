def return_binary_or_hexa(n):
    a = n[34]
    b = n[69]
    sum = 0
    for i in range(a + 1, b):
        if i not in n[34:69]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]