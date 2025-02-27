def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[91]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[13:92]:
            sum += i
    return bin(sum)[2:] if sum % 2 != 0 else hex(sum)[2:].upper()