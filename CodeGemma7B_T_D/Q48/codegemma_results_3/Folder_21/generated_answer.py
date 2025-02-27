def return_binary_or_hexa(a, b):
    sum = 0
    temp = 0
    for i in range(a + 1, b):
        if i not in a and i not in b:
            temp += i
    if temp % 2 != 0:
        return bin(temp)[2:]
    else:
        return hex(temp)[2:].upper()