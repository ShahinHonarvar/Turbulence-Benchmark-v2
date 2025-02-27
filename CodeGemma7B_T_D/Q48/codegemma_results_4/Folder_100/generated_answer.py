def return_binary_or_hexa(n):
    a, b = (n[44], n[78])
    sum = 0
    for i in range(a + 1, b):
        if i not in n[44:79]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()